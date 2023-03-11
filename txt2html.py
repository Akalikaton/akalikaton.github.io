'''ID后一行加#标记，并且转html'''
# 打开原始文件
import codecs
import markdown
import os
file = "0304"
txt_file = "./%s.txt" %file
md_file = "./%s.md" %file
html_file = "./%s.html" %file
with open(txt_file, "r", encoding="utf-8") as file:
    # 读取文件内容并按行分割
    lines = file.readlines()

# 打开输出文件
with open(md_file, "w", encoding="utf-8") as output:
    # 遍历每一行内容
    for i, line in enumerate(lines):
        # 判断当前行是否包含"huaizhi1998@outlook.com"
        if "huaizhi1998@outlook.com" in line:
            # 在"huaizhi1998@outlook.com"的下一行前面加上"# "
            output.write("# " + lines[i+1])
            del lines[i+1]
        else:
            # 将当前行原封不动地写入输出文件
            output.write(line)

css = """
<style>
    body {
        background-color: black;
        color: white;
        font-size: 42px;
    }
    h1 {
        margin-top: 112px;
        font-size: 56px;
        text-decoration:underline
    }
</style>
"""

input_file = codecs.open(md_file, mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)
output_file = codecs.open(html_file, mode="w", encoding="utf-8")
output_file.write(html)
# 在 HTML 中插入 CSS 样式
html_with_css = f"{css}\n{html}"
# print(html_with_css)
# 将 HTML 写入输出文件
with open(html_file, "w", encoding="utf-8") as f:
    # lines=f.readlines()
    # print(lines)
    f.write(html_with_css)

# os.remove(md_file)  