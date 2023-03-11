import os
import pyautogui
import time

# 指定文件夹路径和文件名
folder_path = "D:/Py/html2txt/try"
file_name = "0310.html"

# 拼接完整文件路径
file_path = os.path.join(folder_path, file_name)

# 打开py文件
os.startfile(file_path)

# 等待程序打开
time.sleep(2)

# 复制所有内容
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

# 打开记事本
os.startfile('notepad.exe')

# 等待记事本打开
time.sleep(2)

# 粘贴内容
pyautogui.hotkey('ctrl', 'v')

# 保存文件
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
# pyautogui.typewrite(file_name[:-3] + '.txt')
pyautogui.press('enter')
