import os
import shutil

source_dir = r"E:\25年7-12月收入核查项目提交单-常规组学pdf"
group_size = 50

files = [f for f in os.listdir(source_dir)
         if f.lower().endswith(".pdf")]
files.sort()

print(f"共找到 {len(files)} 个 Word 文件")

for i in range(0, len(files), group_size):
    folder_index = i // group_size + 1
    new_folder = os.path.join(source_dir, str(folder_index))
    os.makedirs(new_folder, exist_ok=True)

    for file in files[i:i + group_size]:
        src = os.path.join(source_dir, file)
        dst = os.path.join(new_folder, file)

        if not os.path.exists(dst):  # 防止重复复制
            shutil.copy2(src, dst)

print("✅ 分组完成（复制模式），原文件未被删除")
