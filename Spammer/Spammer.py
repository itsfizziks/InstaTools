"""
Author: new92
Github: @new92
Leetcode: @new92

Spammer: Python script to spam messages on user(s) on Instagram.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! Spammer requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use Spammer ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 8
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import instagrapi
    import os
    import json
    import requests
    from colorama import init, Fore
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in Spammer have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall Spammer")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('InstaTools'))
                    print(f"[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW

print(f"{GREEN}[✓] Successfully loaded modules !")
sleep(2)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

ANS = ['yes', 'no']

def ScriptInfo():
    with open('config.json') as configFile:
        conf = json.load(configFile)
    f = conf['name'] + '.py'
    fp = os.path.exists(fpath(f)) if not fpath(f) == None else None
    fsize = 0 if fp == None else os.stat(fpath(f)).st_size
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f"{GREEN}[✓] Files and dependencies uninstalled successfully !"

def banner() -> str:
    return f"""{YELLOW}
░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
"""

def checkUser(username:str) -> bool:
    return username in ['', ' '] or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

IDS = []

def main():
    print(banner())
    print("\n")
    print(f"{YELLOW} [-] -- Socials --")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print(f"{YELLOW}[+] Leetcode: @new92")
    print("\n")
    print(f"{YELLOW}[+] Spammer: A python script to spam messages on someone on Instagram.")
    print("\n")
    print(f"{YELLOW}[1] Initiate Spammer")
    print(f"{YELLOW}[2] Show Spammer's info")
    print(f"{YELLOW}[3] Uninstall Spammer")
    print(f"{YELLOW}[4] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 4:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-4]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        client = instagrapi.Client()
        msg = 'hello world'
        username=str(input(f"{YELLOW}[::] Please enter your username: "))
        while checkUser(username):
            print(f"{RED}[!] Invalid username !")
            sleep(1)
            username=str(input(f"{YELLOW}[::] Please enter again your username: "))
        while valUser(username):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Uninstall and Exit")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Uninstall and Exit")
                opt=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[::] Please enter the username: "))
                while checkUser(username):
                    print(f"{RED}[!] Invalid username !")
                    sleep(1)
                    username=str(input(f"{YELLOW}[::] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Thank you for using Spammer 😁")
                sleep(2)
                print(f"{YELLOW}[+] Until next time 👋")
                sleep(1)
                quit(0)
        username = username.lower().strip()
        password=str(input(f"{YELLOW}[::] Please enter your password: "))
        while password in ['', ' ']:
            print(f"{RED}[!] Invalid password !")
            sleep(1)
            password=str(input(f"{YELLOW}[::] Please enter again your password: "))
        password = password.strip()
        try:
            client.login(username,password)
        except Exception as ex:
            print(f"{RED}[!] Login error !")
            sleep(1)
            print(f"{YELLOW}[*] Error message ==> {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        sleep(1)
        count=int(input(f"{YELLOW}[::] Number of targets: "))
        while count < 1:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            count=int(input(f"{YELLOW}[::] Number of targets: "))
        for i in range(count):
            user=str(input(f"{YELLOW}[::] Please enter the target username: "))
            while checkUser(user) or valUser(user):
                print(f"{RED}[!] Invalid username !")
                sleep(1)
                user=str(input(f"{YELLOW}[::] Please enter again the target username: "))
            user=user.lower().strip()
            IDS.append(requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis').json()["logging_page_id"].strip("profilePage_"))
        sleep(1)
        print(f"{YELLOW}[+] Default message: {msg}")
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: {ANS}")
        sleep(2)
        change=str(input(f"{YELLOW}[?] Change message ? "))
        while change.lower() not in ANS or change in ['', ' ']:
            print(f'{RED}[!] Invalid answer !')
            sleep(1)
            print(f"{GREEN}[+] Acceptable answers: {ANS}")
            sleep(2)
            change=str(input(f"{YELLOW}[?] Change message ? "))
        if change.lower() == ANS[0]:
            sleep(1)
            msg=str(input(f"{YELLOW}[::] Please enter the message: "))
            sleep(2)
        msgs = 0
        sleep(1)
        print(f"{GREEN}[+] To stop enter: <Ctrl + C>")
        sleep(2.5)
        while True:
            client.direct_send(msg,IDS)
            sleep(1)
            print("[✓] Message Sent !")
            msgs += 1
        print(f"{GREEN}[✓] Successfully sent {msgs} to {len(IDS)} users.")
        sleep(2)
    
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(4)
        print("\n\n")

    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Spammer 😁")
        sleep(2)
        print(f"{GREEN}[+] Until next time 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Spammer 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit(0)

    print(f"{YELLOW}[1] Back to menu")
    print(f"{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 2:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    if num == 1:
        clear()
        main()
    else:
        print(f"{GREEN}[+] Thank you for using Spammer 😃")
        sleep(2)
        print(f"{GREEN}[+] Until next time 🤗")
        sleep(1)
        print(f"{YELLOW}[+] Exiting...")
        quit(0)

if __name__ == '__main__':
    main()