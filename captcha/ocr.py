#!/usr/bin/env python
import base64
import cgi
import uuid
import subprocess
import os

form = cgi.FieldStorage();
data = base64.b64decode(form.getfirst('data', '').replace(" ", "+"))

png = '/tmp/'+str(uuid.uuid4()).replace('-', '') + '.png'
pbm = '/tmp/'+str(uuid.uuid4()).replace('-', '') + '.pbm'
tif = '/tmp/'+str(uuid.uuid4()).replace('-', '') + '.tif'
txt = '/tmp/'+str(uuid.uuid4()).replace('-', '')

f = open(png, "w")
f.write(data)
f.close()

os.system("convert " + png + " " + pbm)
os.system("convert " + pbm + " " + tif)

os.system("tesseract " + tif + " " + txt)

f = open(txt + ".txt", "r")
code = f.read()


os.remove(png)
os.remove(pbm)
os.remove(tif)
os.remove(txt + ".txt")

print """\
Content-Type: text/plain\n
"""

print code
