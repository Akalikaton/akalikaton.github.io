py.exe .\txt2html.py

py.exe .\Gindex.py

rm .\raw\*.md
Move-Item .\raw\*.txt .\raw\done\
