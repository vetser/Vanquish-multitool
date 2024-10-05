import os, sys, random, string, time

try:
    import colorama
    import threading
    import requests
    import pystyle
except ModuleNotFoundError:
    os.system('pip install colorama')
    os.system('pip install requests')
    os.system('pip install pystyle')

from pystyle import Colors, Colorate, Center, Write, System
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore
from dhooks import Webhook
from __init__ import *


# ---------

banner = f"""
                                                 ╦  ╦┌─┐┌┐┌╔═╗ ┬ ┬┬┌─┐┬ ┬ [!!] Made with love by vetser 
                                                 ╚╗╔╝├─┤│││║═╬╗│ ││└─┐├─┤ [99] Exit
                                                  ╚╝ ┴ ┴┘└┘╚═╝╚└─┘┴└─┘┴ ┴ [00] Refresh interface"""

def main():

# ---------
   clear()
   size()
# ---------

   System.Title('Vanquish')
   options = f"""                                                 [1] > Token Checker 
                                                 [2] > Hook Spammer
                                                 [3] > Hook Deleter
                                                 [4] > Nitro Gen"""
   print(Colorate.Horizontal(Colors.blue_to_cyan, banner))
   print(Colorate.Horizontal(Colors.blue_to_white, options))
   choice = input(f"{Colors.s}vanquish@raider:$ ~ option : ")

   if choice == "1":
      token_checker()
      exit = input(f"{Colors.s}[#] Vanquish | Press enter")
      exit = main()
  
   elif choice == "2":
      webhook_spam()
      exit = input(f"{Colors.s}[#] Vanquish | Press enter")
      exit = main()
# ---------

   elif choice == "3":
      clear()
      size()
      Titles.deletor_title()
      print(Colorate.Horizontal(Colors.blue_to_cyan, banner))

    # ---------
      webhook = str(input(f"{Colors.s}vanquish@raider:$ {Colors.z}[Hidden]{Colors.z}{Colors.s} ~ webhook : {Colors.o}"))
      response = requests.delete(webhook)

    # ---------
      exit = input(f"{Colors.s}[#] Vanquish | Press enter")
      exit = main
   
   elif choice == "4":
      nitro_gen()
      exit = input(f"{Colors.s}[#] Vanquish | Press enter")

   elif choice == "99":
      clear()
      main()

   elif choice == "00":
      sys.exit()
   
if __name__ == "__main__":
    main()