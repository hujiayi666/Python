from flask import Flask,render_template

app=Flask(__name__)
hero=["黑暗之女",
"狂战士",
"正义巨像",
"卡牌大师",
"德邦总管",
"无畏战车",
"诡术妖姬",
"猩红收割者",
"远古恐惧",
"正义天使",
"无极剑圣"]
@app.route("/index")
def index():
    return render_template('index.html',hero1=hero)

app.run(debug=True)

















