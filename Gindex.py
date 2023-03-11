import os

# 指定data文件夹的路径
data_folder = './htmldata'

# 获取data文件夹中所有文件的文件名
file_names = os.listdir(data_folder)

# 生成HTML代码
html = '<!DOCTYPE html>\n<html>\n  <head>\n    <title>My Data Files</title>\n  </head>\n  <body>\n    <h1>My Data Files</h1>\n    <ul>\n'
for file_name in file_names:
    html += f'      <li><a href="{data_folder}/{file_name}">{file_name}</a></li>\n'
html += '    </ul>\n  </body>\n</html>'

# 将HTML代码写入index.html文件中
with open('index.html', 'w') as f:
    f.write(html)
    