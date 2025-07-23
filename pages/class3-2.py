# r讀檔案，檔案不存在，回報錯誤
# w寫檔案，檔案不存在，創建檔案
# a续寫檔案，檔案不存在，創建檔案
f = open("pages/class1-1.py", "r", encoding="utf-8")  # 開啟檔案
content = f.read()  # 讀取內容
print(content)  # 印出內容
f.close()  # 關閉檔案

print("-" * 10)

with open("pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # 印出內容
# 不用寫f.ciose(),with自動幫你關好

filename = "class1.md"
print(filename.endswith(".md"))  # True

import os

folderPath = "markdown"
files = os.listdir(folderPath)
print(files)
