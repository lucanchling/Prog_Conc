import os
import sys

pid = os.fork()
arg = sys.argv[1:]

os.execlp('python3', 'python3', 'salut.py','1','2','3')
os._exit(0)