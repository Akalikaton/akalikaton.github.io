'''ID后一行加#标记，并且转html'''
# 打开原始文件
import codecs
import markdown
import os
for filename in os.listdir("./raw"):
    if filename.endswith(".txt"):
        file = filename.split(".")[0]
        txt_file = "./raw/%s.txt" %file
        md_file = "./raw/%s.md" %file
        html_file = "./htmldata/%s.html" %file
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
                font-size: 56px;
            }
            h1 {
                margin-top: 144px;
                font-size: 72px;
                text-decoration:underline
            }
        </style>
        """

        input_file = codecs.open(md_file, mode="r", encoding="utf-8")
        text = input_file.read()
        html = markdown.markdown(text)
        with codecs.open(html_file, mode="w", encoding="utf-8") as output_file:
            output_file.write(html)
        # 在 HTML 中插入 CSS 样式
        html_with_css = f"{css}"
        # print(html_with_css)
        # 将 HTML 写入输出文件
        with open(html_file, "a", encoding="utf-8") as f:

            f.write(html_with_css)

        # os.remove(md_file)  