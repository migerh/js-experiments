import base64
import cgi

form = cgi.FieldStorage();
data = base64.b64decode(form.getfirst('data', ''))
png = '/tmp/'+str(uuid.uuid4()) + '.png'
pbm = '/tmp/'+str(uuid.uuid4()) + '.pbm'
tif = '/tmp/'+str(uuid.uuid4()) + '.tif'
txt = '/tmp/'+str(uuid.uuid4()) + '.txt'

f = open(png, "w")
f.write(data)

pngtopbm_process = subprocess.Popen(["convert", png, pbm], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
pngtopbm.communicate('')[0]
pbmtotif_process = subprocess.Popen(["convert", pbm, tif], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
pbmtotif.communicate('')[0]
tiftotxt_process = subprocess.Popen(["tesseract", tif, txt], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
tiftotxt.communicate('')[0]
cattxt_process = subprocess.Popen(["cat", txt], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
code = cattxt.communicate('')[0]

os.remove(png)
os.remove(pbm)
os.remove(tif)
os.remove(txt)

print """\
Content-Type: text/plain\n
"""

print code
