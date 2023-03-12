import os

# 指定data文件夹的路径
data_folder = './htmldata'

# 获取data文件夹中所有文件的文件名
file_names = os.listdir(data_folder)

# 生成HTML代码
html = '<!DOCTYPE html>\n<html>\n  <head>\n    <title>UA Deutsch Lernen</title>\n  </head>\n  <body>\n    <h1>UA Deutsch Lernen</h1>\n    <ul>\n'
for file_name in file_names:
    html += f'      <li><a href="{data_folder}/{file_name}">{file_name}</a></li>\n'
html += '    </ul>\n  </body>\n</html>'

# 将HTML代码写入index.html文件中
with open('index.html', 'w') as f:
    f.write(html)
    
css = """
        <style>
            body {
                background-color: black;
                color: white;
                font-size: 42px;
            }
            h1 {
                font-size: 56px;
                text-decoration:underline
            }
        </style>
        """
# 在 HTML 中插入 CSS 样式
html_with_css = f"{css}"
        # print(html_with_css)
        # 将 HTML 写入输出文件
with open("index.html", "a", encoding="utf-8") as f:

    f.write(html_with_css)