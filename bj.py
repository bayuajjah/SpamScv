import os
import sys
from time import sleep
import random
import time
M = '\033[031m'
H = '\033[032m'
K = '\033[033m'
B = '\033[034m'
BM = '\033[036m'
os.system('clear')
sleep(1)
def TheX(s):
  for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
TheX(H + 'SELAMAT DATANG DI TOOLS Apmz channel')
TheX('Sebelum memasuki Toolsnya Silahkan ')
TheX('Kalian Subscribe Dulu Youtube Apmz Channel')
TheX('Supaya Kalian Dapat Info Terbaru Dari Channel saya')
TheX('1')
TheX('2')
TheX('3')
os.system('xdg-open https://www.youtube.com/channel/UCS4EpzW-9kWTIt3Dmzb4oQQ')
os.system('clear')
sleep(0.1)
def main(s):
  for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() + 0.4)
print (K + 'Loading..')
sleep(1)
main(B + '  >>>>>>>>>')
sleep(1)
os.system('clear')
sleep(1)
main = input('Hallo siapa nama tuan:')
sleep(1)
print (H + 'Hallo selamat datang tuan',main)
sleep(1)
print (M + 'Jangan lupa subscribe Youtube Apmz channel^_^')
sleep(1)
os.system('php s-SpamOtp.php')
sleep(1)
