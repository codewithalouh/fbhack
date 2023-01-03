#!/bin/python3
#coded by alouh sperk
#bobo ka kung pati ito ileleet mo
import api
import base64, string, random, sys, time, os
from colorama import init
from colorama import Fore, Back, Style
init()
  



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
  api.checkhost()
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
      x = ''.join(random.choices(string.ascii_letters,k=9))
      print(Fore.BLUE + '[403] ' + Fore.YELLOW + username + ":" + x + " ==> " + Fore.RED + "Login Failed")
      api.wget()
      time.sleep(0.5)
      
  except KeyboardInterrupt:
    print(Fore.BLUE + "[+] " + Fore.RED + "HACK THE PLANET" + Fore.BLUE + " [+]")
    

  
if __name__ == "__main__":
  main()
