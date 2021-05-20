import os

(dfr,dfw) = os.pipe()

cat = os.fork()


if cat != 0:
    os.close(dfr)
    os.dup2(dfw,1)
    os.close(dfw)
    os.execlp("cat","cat","test.txt")
else:
    os.close(dfw)
    os.dup2(dfr,0)
    os.close(dfr)
    os.execlp("wc","wc")

os.exit(0)
