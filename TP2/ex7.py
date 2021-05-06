from os import fork, wait
import sys


N = 3
for i in range(N):
    fork()
    fork()
print('Bonjour')
sys.exit(0)

# pour compter le nombre de liugne affichées dans le shell :
# python3 ex7.py | wc -l