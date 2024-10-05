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
from vanquish import *

class Titles:
    def nitro_title():
        System.Title('Vanquish Nitro gen')
# ---------

    def checker_title():
        System.Title('Vanquish Token checker')
# ---------

    def deletor_title():
        System.Title('Vanquish Webhook deletor')
# ---------

    def webhook_spammer_title():
        System.Title('Vanquish Webhook Spammer')

class Colors:
    c: str = Fore.RED
    s: str = Fore.BLUE
    o: str = Fore.BLACK
    z: str = Fore.LIGHTBLACK_EX
    k: str = Fore.LIGHTGREEN_EX
    l: str = Fore.LIGHTRED_EX
    blue_to_cyan: str = Colors.blue_to_cyan
    blue_to_white: str = Colors.blue_to_white
    green_to_white: str = Colors.green_to_white
    red_to_white: str = Colors.red_to_white
    red_to_yellow: str = Colors.red_to_yellow

# ---------

def clear():
    System.Clear()

def size():
    System.Size(126, 26)

# ---------


def token_checker():
    clear()
    size()
    Titles.checker_title()
    
    # ---------
    print(Colorate.Horizontal(Colors.blue_to_cyan, banner))
    
    try:
        with open("input/tokens.txt", "r") as file:
            tokens = file.readlines()
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.red_to_white, "Error: 'input/tokens.txt' not found."))
        return
    
    for token in tokens:
        token = token.strip()
        
        if not token:
            continue
        
        headers = {
            'Authorization': token  # headers
        }
        
        try:
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            status_code = r.status_code
            
            if status_code == 401:
                print(Colorate.Horizontal(Colors.red_to_white, f"Vanquish | Token Checker | Logging | [{status_code}] | Invalid | {token[:12]}"))
            elif status_code == 200:
                print(Colorate.Horizontal(Colors.green_to_white, f"Vanquish | Token Checker | Logging | [{status_code}] | Valid | {token[:12]}"))
            else:
                print(f"Error: Unexpected status code {status_code}")
        
        except Exception as e:
            print(f"Error: {e}")

def webhook_spam():
    clear()
    Titles.webhook_spammer_title()
    print(Colorate.Horizontal(Colors.blue_to_cyan, banner))
    webhook = input(f"{Colors.s}vanquish@raider:$ {Colors.z}[Hidden]{Colors.z}{Colors.s} ~ webhook : {Colors.o}")

    hook = Webhook(webhook)

    message = input(f"{Colors.s}vanquish@raider:$ ~ message : ")
    
    while True:
        hook.send(f"{message}")

def nitro_gen():
    clear()
    Titles.nitro_title()
    size()
    print(Colorate.Horizontal(Colors.blue_to_cyan, banner))
    
    while True:
        rand_str = ''.join(random.choices(string.ascii_letters, k=16))
        print(Colorate.Horizontal(Colors.green_to_white, f"Vanquish | Nitro gen | Logging | Success | Generated nitro: https://discord.gift/{rand_str}"))
        time.sleep(1)