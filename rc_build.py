import subprocess, os

images = os.listdir('./rc/icons')
qss = os.listdir('./rc/qss')
f = open('./rc/rc.qrc', 'w+')
f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

for item in images:
    f.write(u'<file alias="icons/'+ item +'">icons/'+ item +'</file>\n')

for item in qss:
    f.write(u'<file alias="qss/'+ item +'">qss/'+ item +'</file>\n')

f.write(u'</qresource>\n</RCC>')
f.close()

pipe = subprocess.Popen(r'pyrcc5 -o rc.py ./rc/rc.qrc', stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, creationflags=0x08)