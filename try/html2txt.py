from bs4 import BeautifulSoup
import re
import os

# 要转换的文件夹路径
folder_path = "D:/Py/html2txt/try"

# 将所有HTML文件转换为TXT文件
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        # 读取HTML文件内容
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
            html_content = f.read()

        # 使用BeautifulSoup解析HTML文件，并获取所有文本内容
        soup = BeautifulSoup(html_content, "html.parser")
        text_content = soup.get_text()

        # 删除所有空行和多余空格
        text_content = re.sub(r"\n\s*\n", "\n", text_content)
        text_content = re.sub(r"\s{2,}", " ", text_content)

        # 写入TXT文件
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(folder_path, txt_filename), "w", encoding="utf-8") as f:
            f.write(text_content)
