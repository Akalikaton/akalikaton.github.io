'''修改txt文件，添加标记'''
import os

# 要处理的文件路径
file_path = "D:/Py/html2txt/try/0310.txt"
new_path = "D:/Py/html2txt/try/0310new.txt"
# 读取文件内容
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
# 删除"Regenerate response"后所有内容
for i, line in enumerate(lines):
    if "Regenerate response" in line:
        lines = lines[:i]
        break

# 在“huaizhi1998@outlook.com”后一行前添加“# ”
i = 0
for line in lines:
    if "huaizhi1998@outlook.com" in line:
        #lines.insert(i, "# " + line)
        i = i+1
        print(i)
        print(line)
        # break
# print(len(lines))
# 删除“huaizhi1998@outlook.com”
#lines = [line for line in lines if "huaizhi1998@outlook.com" not in line]

# 删除多余空行，最多保留一行空行
new_lines = []
prev_line_blank = False
for line in lines:
    if not line.strip():
        if not prev_line_blank:
            new_lines.append(line)
            prev_line_blank = True
    else:
        new_lines.append(line)
        prev_line_blank = False

# 将新的文本写回文件
with open(new_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
