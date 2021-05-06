import os,sys

msg = "MonMessage"

(dfr,dfw) = os.pipe()
n = os.write(dfw,msg)
msgRecu = os.read(dfr,len(msg))
os.close(dfr)
os.close(dfw)
sys.exit(0)