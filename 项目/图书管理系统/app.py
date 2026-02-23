from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "books.json"

# ====== 工具函数（等价于全局 book[]） ======
def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

# ====== 1. 登记书籍（RegisterBooks） ======
@app.route("/register", methods=["POST"])
def register_books():
    book = request.json
    books = load_books()

    for b in books:
        if b["id"] == book["id"]:
            return {"msg": "ID 已存在"}, 400

    book["borrow"] = 1
    book["borrow_total"] = 0
    book["return_total"] = 0
    books.append(book)
    save_books(books)
    return {"msg": "登记成功"}

# ====== 2. 浏览书籍（ShowBook） ======
@app.route("/books", methods=["GET"])
def show_books():
    return jsonify(load_books())

# ====== 3. 借阅书籍（BorrowBooks） ======
@app.route("/borrow", methods=["POST"])
def borrow_book():
    data = request.json
    books = load_books()

    for b in books:
        if b["id"] == data["id"]:
            if b["borrow"] == 0 or b["number"] < data["count"]:
                return {"msg": "不可借或库存不足"}, 400
            b["number"] -= data["count"]
            b["borrow_total"] += data["count"]
            if b["number"] == 0:
                b["borrow"] = 0
            save_books(books)
            return {"msg": "借阅成功"}
    return {"msg": "未找到书籍"}, 404

# ====== 4. 归还书籍（ReturnBooks） ======
@app.route("/return", methods=["POST"])
def return_book():
    data = request.json
    books = load_books()

    for b in books:
        if b["id"] == data["id"]:
            unreturned = b["borrow_total"] - b["return_total"]
            if data["count"] > unreturned:
                return {"msg": "归还数量错误"}, 400
            b["number"] += data["count"]
            b["return_total"] += data["count"]
            b["borrow"] = 1
            save_books(books)
            return {"msg": "归还成功"}
    return {"msg": "未找到书籍"}, 404

# ====== 5. 书籍排序（SortByID） ======
@app.route("/sort", methods=["GET"])
def sort_books():
    order = request.args.get("order", "asc")
    books = load_books()
    books.sort(key=lambda x: x["id"], reverse=(order == "desc"))
    return jsonify(books)

# ====== 6. 删除书籍（Delete） ======
@app.route("/delete/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    books = load_books()
    books = [b for b in books if b["id"] != book_id]
    save_books(books)
    return {"msg": "删除成功"}

# ====== 7. 查找书籍（Searching） ======
@app.route("/search/<book_id>", methods=["GET"])
def search_book(book_id):
    for b in load_books():
        if b["id"] == book_id:
            return jsonify(b)
    return {"msg": "未找到"}, 404

app.run(debug=True)
