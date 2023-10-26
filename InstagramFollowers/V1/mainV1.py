# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92

IGFI: Use this script to increase the followers of an Insta account


*********IMPORTANT*********
User's login credentials (username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's Instagram account
***************************
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! IGFI requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IGFI ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'os', 'platform', 'rich', 'instagrapi', 'requests', 'json', 'instaloader', 'datetime', 'colorama', 'logging']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.8)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay')
    import platform
    from os import system
    import instagrapi
    import requests
    import os
    import json
    import logging
    import instaloader
    from datetime import datetime
    from colorama import init, Fore
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in IGFI have been installed !")
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
                print(f"[*] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                valErr = opt in [1,2]
                while not valErr:
                    try:
                        print("[1] Uninstall script")
                        print("[2] Exit")
                        opt=int(input("[>] Please enter again a number (from the above ones): "))
                        valErr = opt in [1,2]
                    except ValueError:
                        print("[!] Please enter a valid number.")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                        sleep(1)
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in dirs:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('IGFI'))
                    print("[✓] Files and dependencies uninstalled successfully !")
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
YELLOW = Fore.YELLOW
RED = Fore.RED

sleep(0.8)
console.clear()
console.print("[bold dark_green][✓] Successfully loaded modules.")
sleep(1.1)
console.clear()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in dirs:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    with open('InstagramFollowers/V1/config.json') as config:
        conf = json.load(config)
    f = 'mainV1.py'
    fp = True if not fpath(f) == None else False
    fsize = 0 if not fp else os.stat(fpath(f)).st_size
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
    print(f"{YELLOW}[+] PyPI: @{conf['author']}")
    print(f"{YELLOW}[+] Contributors : {conf['contributors']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}[+] Latest update: {conf['update']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {fpath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

def banner() -> str:
    console.print("""[bold yellow]
                                                ██╗░██████╗░███████╗██╗     ██╗░░░██╗░░███╗░░
                                                ██║██╔════╝░██╔════╝██║     ██║░░░██║░████║░░
                                                ██║██║░░██╗░█████╗░░██║     ╚██╗░██╔╝██╔██║░░
                                                ██║██║░░╚██╗██╔══╝░░██║     ░╚████╔╝░╚═╝██║░░
                                                ██║╚██████╔╝██║░░░░░██║     ░░╚██╔╝░░███████╗
                                                ╚═╝░╚═════╝░╚═╝░░░░░╚═╝     ░░░╚═╝░░░╚══════╝
[/]""")

ANS = ["yes","no"]

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ],
    [
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ],
    [
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ],
    [
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    ]
]

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

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
    rmdir(fpath('IGFI'))
    return f"{GREEN}[✓] Files and dependencies uninstalled successfully !"

def checkUser(username:str) -> bool:
    return username in ['', ' '] or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def nums():
    console.print("[bold yellow][1] Increase followers[/]")
    console.print("[bold yellow][2] Show IGFI's info[/]")
    console.print("[bold yellow][3] Clear log[/]")
    console.print("[bold yellow][4] Uninstall IGFI[/]")
    console.print("[bold yellow][5] Exit[/]")

def main():
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] IGFI is a python script for increasing the number of followers of an Instagram account.")
    print("\n")
    nums()
    print("\n")
    option=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    valErr = option in [1,2,3,4,5]
    while not valErr:
        try:
            nums()
            print('\n')
            option=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
            valErr = option in [1,2,3,4,5]
        except ValueError:
            print(f"{RED}[!] Please enter a valid number.")
            sleep(1)
            print(f"{GREEN}[+] Acceptable numbers: [1,2,3,4,5]")
            sleep(1)
    if option == 1:
        clear()
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        keep=str(input(f"{YELLOW}[?] Keep log ? "))
        while keep.lower() not in ANS or keep in ['', ' ']:
            if keep in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(1)
            keep=str(input(f"{YELLOW}[?] Keep log ? "))
        keep = True if keep.lower() == ANS[0] else False
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        check=str(input(f"{YELLOW}[?] Display the usernames of the followers added ? "))
        while check.lower() not in ANS or check in ['', ' ']:
            if check in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            check=str(input(f"{YELLOW}[?] Display the usernames of the followers added ? "))
        check = True if check.lower() == ANS[0] else False
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        while con.lower() not in ANS or con in ['', ' ']:
            if con in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        if con.lower() == ANS[0]:
            logging.basicConfig(
                filename='cons.txt',
                level=logging.INFO,
                format='%(asctime)s [%(levelname)s]: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.')
        else:
            print(f"{YELLOW}[OK]")
            sleep(1)
            print(f"{YELLOW}[1] Exit")
            print(f"{YELLOW}[2] Uninstall IGFI and exit")
            num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            valErr = num in [1,2]
            while not valErr:
                try:
                    print(f"{YELLOW}[1] Exit")
                    print(f"{YELLOW}[2] Uninstall IGFI and exit")
                    sleep(1)
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                    valErr = num in [1,2]
                except ValueError:
                    print(f"{RED}[!] Please enter a valid number.")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1,2]")
                    sleep(1)
            if num == 1:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{YELLOW}[+] Thank you for using IGFI 🫡")
                sleep(2)
                print(f"{YELLOW}[+] Until we meet again 👋")
                sleep(1)
                quit(0)
        sleep(1)
        clear()
        print(f"{YELLOW}[+] The login credentials will not be stored or saved")
        sleep(2)
        print(f"{GREEN}|--------------------|LOGIN|--------------------|")
        username=str(input(f"{YELLOW}[>] Please enter your username: "))
        username = username.lower().strip()
        while checkUser(username):
            if username in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length !")
                sleep(1)
                print(f"{YELLOW}[+] The length of the username must be less than or equal to 30 characters.")
            sleep(1)
            username=str(input(f"{YELLOW}[>] Please enter again your username: "))
        while valUser(username):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            opt=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            valErr = opt in [1,2,3]
            while not valErr:
                try:
                    print(f"{YELLOW}[1] Try with another username")
                    print(f"{YELLOW}[2] Return to menu")
                    print(f"{YELLOW}[3] Exit")
                    opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
                    valErr = opt in [1,2,3]
                except ValueError:
                    print(f"{RED}[!] Please enter a valid number.")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1,2,3]")
                    sleep(1)
            if opt == 1:
                clear()
                username=str(input(f"{YELLOW}[>] Please enter the username: "))
                username = username.lower().strip()
                while checkUser(username):
                    if username in ['', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid username !")
                        sleep(1)
                        print(f"{GREEN}[+] The length of the username must be lower than or equal to 30 characters.")
                    sleep(1)
                    username=str(input(f"{YELLOW}[>] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(f"{YELLOW}[+] Thank you for using IGFI 😁")
                sleep(2)
                print(f"{YELLOW}[+] See you next time 👋")
                sleep(1)
                quit(0)
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        ga=str(input(f"{YELLOW}[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? "))
        while ga.lower() not in ANS or ga in ['', ' ']:
            if ga in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(1)
            ga=str(input(f"{YELLOW}[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? "))
        ga = True if ga.lower() == ANS[0] else False
        if ga:
            loader = instaloader.Instaloader()
            try:
                loader.load_session_from_file(username)
            except FileNotFoundError:
                print(f"{RED}[✕] Session file not found !")
                sleep(2)
                print(f"{GREEN}[+] Logging in...")
                sleep(0.8)
            if not loader.context.is_logged_in:
                loader.interactive_login(username)
                loader.save_session_to_file()
            profile = instaloader.Profile.from_username(loader.context, username)
            followers_bef = profile.followers
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
        sleep(1)
        password=str(input(f"{YELLOW}[>] Please enter your password: "))
        while password in ['', ' ']:
            print(f"{RED}[!] This field can't be blank !")
            sleep(1)
            password=str(input(f"{YELLOW}[>] Please enter again your password: "))
        password=password.strip()
        sleep(1)
        print(f"{GREEN}|---------------------------------------------|")
        client=instagrapi.Client()
        try:
            login = client.login(username,password)
            if login:
                print(f"{GREEN}[✓] Login successful !")
                sleep(2)
                print(f"{YELLOW}[+] Please wait while the program is increasing your followers...")
            else:
                print(f"{RED}[×] Login unsuccessful !")
                sleep(2)
                print(f"{YELLOW}[+] Please check the username and/or the password !")
                sleep(1)
                print(f"{YELLOW}[1] Return to menu")
                print(f"{YELLOW}[2] Exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                valErr = num in [1,2]
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Return to menu")
                        print(f"{YELLOW}[2] Exit")
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                        valErr = num in [1,2]
                    except ValueError:
                        print(f"{RED}[!] Please enter a valid number.")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable numbers: [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    main()
                else:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        except Exception as ex:
            print(f"{RED}[!] Error !")
            sleep(1)
            print(f"{YELLOW}[=] Error message -> {ex}")
            sleep(2)
            print(f"{GREEN}[1] Return to menu")
            print(f"{GREEN}[2] Exit")
            num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            valErr = num in [1,2]
            while not valErr:
                try:
                    print(f"{YELLOW}[1] Return to menu")
                    print(f"{YELLOW}[2] Exit")
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                    valErr = num in [1,2]
                except ValueError:
                    print(f"{RED}[!] Please enter a valid number.")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1,2]")
                    sleep(1)
            if num == 1:
                clear()
                main()
            else:
                clear()
                print(f"{RED}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(1)
                quit(0)
        sleep(2)
        clear()
        print(f"{YELLOW}[+] To end the process enter: <Ctrl + C>")
        sleep(2)
        print(f"{YELLOW}[*] NOTE: Use this program every 2 days in order for your account not to get blocked")
        sleep(6)
        clear()
        follow = 0
        unfollow = 0
        while True:
            try:
                client.user_follow(173560420) #Cristiano Ronaldo
                follow += 1
                print(f"{YELLOW}[+] Following 173560420...")
                sleep(2)
                client.user_follow(1436859892) #Cardi B
                follow += 1
                print(f"{YELLOW}[+] Following 1436859892...")
                sleep(2)
                client.user_follow(18428658) #Kim Kardashian
                follow += 1
                print(f"{YELLOW}[+] Following 18428658...")
                sleep(2)
                client.user_follow(7719696) #Ariana Grande
                follow += 1
                print(f"{YELLOW}[+] Following 7719696...")
                sleep(2)
                client.user_follow(451573056) #Nicki Minaj
                follow += 1
                print(f"{YELLOW}[+] Following 451573056...")
                sleep(2)
                client.user_follow(247944034) #Beyonce
                follow += 1
                print(f"{YELLOW}[+] Following 247944034...")
                sleep(2)
                client.user_follow(407964088) #Katy Perry
                follow += 1
                print(f"{YELLOW}[+] Following 407964088...")
                sleep(2)
                client.user_follow(460563723) #Selena Gomez
                follow += 1
                print(f"{YELLOW}[+] Following 460563723...")
                sleep(2)
                client.user_follow(6860189) #Justin Bieber
                follow += 1
                print(f"{YELLOW}[+] Following 6860189...")
                sleep(2)
                client.user_follow(427553890) #Lionel Messi
                follow += 1
                print(f"{YELLOW}[+] Following 427553890...")
                sleep(2)
                client.user_follow(26669533) #Neymar Jr
                follow += 1
                print(f"{YELLOW}[+] Following 26669533...")
                sleep(2)
                client.user_follow(4213518589) #Kylian Mbappe
                follow += 1
                print(f"{YELLOW}[+] Following 4213518589...")
                sleep(2)
                client.user_follow(12331195) #Dua Lipa
                follow += 1
                print(f"{YELLOW}[+] Following 12331195...")
                sleep(2)
                client.user_follow(28527810) #Billie Eilish
                follow += 1
                print(f"{YELLOW}[+] Following 28527810...")
                sleep(2)
                client.user_follow(12281817) #Kylie Jenner
                follow += 1
                print(f"{YELLOW}[+] Following 12281817...")
                sleep(2)
                client.user_follow(208560325) #Khloe Kardashian
                follow += 1
                print(f"{YELLOW}[+] Following 208560325...")
                sleep(2)
                client.user_follow(145821237) #Kourtney Kardashian
                follow += 1
                print(f"{YELLOW}[+] Following 145821237...")
                sleep(2)
                client.user_follow(305701719) #Jennifer Lopez
                follow += 1
                print(f"{YELLOW}[+] Following 305701719...")
                sleep(2)
                client.user_follow(217867189) #Shakira
                follow += 1
                print(f"{YELLOW}[+] Following 217867189...")
                sleep(2)
                client.user_follow(25025320) #Instagram
                follow += 1
                print(f"{YELLOW}[+] Following 25025320...")
                sleep(2)
                client.user_follow(787132) #National Geographic
                follow += 1
                print(f"{YELLOW}[+] Following 787132...")
                sleep(2)
                client.user_follow(260375673) #FC Barcelona
                follow += 1
                print(f"{YELLOW}[+] Following 260375673...")
                sleep(2)
                client.user_follow(290023231) #Real Madrid
                follow += 1
                print(f"{YELLOW}[+] Following 290023231...")
                sleep(2)
                client.user_follow(1269788896) #Champions League
                follow += 1
                print(f"{YELLOW}[+] Following 1269788896...")
                sleep(2)
                client.user_follow(29394004) #Chris Brown
                follow += 1
                print(f"{YELLOW}[+] Following 29394004...")
                sleep(2)
                client.user_follow(11830955) #Taylor Swift
                follow += 1
                print(f"{YELLOW}[+] Following 11830955...")
                sleep(2)
                client.user_follow(6380930) #Kendall Jenner
                follow += 1
                print(f"{YELLOW}[+] Following 6380930...")
                sleep(2)
                client.user_follow(2094200507) #Virat Kohli
                follow += 1
                print(f"{YELLOW}[+] Following 2094200507...")
                sleep(2)
                client.user_follow(9777455) #Zendaya
                follow += 1
                print(f"{YELLOW}[+] Following 9777455...")
                sleep(2)
                client.user_unfollow(173560420) #Cristiano Ronaldo
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 173560420...")
                sleep(2)
                client.user_unfollow(1436859892) #Cardi B
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 1436859892...")
                sleep(2)
                client.user_unfollow(18428658) #Kim Kardashian
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 18428658...")
                sleep(2)
                client.user_unfollow(7719696) #Ariana Grande
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 7719696...")
                sleep(2)
                client.user_unfollow(451573056) #Nicki Minaj
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 451573056...")
                sleep(2)
                client.user_unfollow(247944034) #Beyonce
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 247944034...")
                sleep(2)
                client.user_unfollow(407964088) #Katy Perry
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 407964088...")
                sleep(2)
                client.user_unfollow(460563723) #Selena Gomez
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 460563723...")
                sleep(2)
                client.user_unfollow(6860189) #Justin Bieber
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 6860189...")
                sleep(2)
                client.user_unfollow(427553890) #Lionel Messi
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 427553890...")
                sleep(2)
                client.user_unfollow(26669533) #Neymar Jr
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 26669533...")
                sleep(2)
                client.user_unfollow(4213518589) #Kylian Mbappe
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 4213518589...")
                sleep(2)
                client.user_unfollow(12331195) #Dua Lipa
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 12331195...")
                sleep(2)
                client.user_unfollow(28527810) #Billie Eilish
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 28527810...")
                sleep(2)
                client.user_unfollow(12281817) #Kylie Jenner
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 12281817...")
                sleep(2)
                client.user_unfollow(208560325) #Khloe Kardashian
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 208560325...")
                sleep(2)
                client.user_unfollow(145821237) #Kourtney Kardashian
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 145821237...")
                sleep(2)
                client.user_unfollow(305701719) #Jennifer Lopez
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 305701719...")
                sleep(2)
                client.user_unfollow(217867189) #Shakira
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 217867189...")
                sleep(2)
                client.user_unfollow(25025320) #Instagram
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 25025320...")
                sleep(2)
                client.user_unfollow(787132) #National Geographic
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 787132...")
                sleep(2)
                client.user_unfollow(260375673) #FC Barcelona
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 260375673...")
                sleep(2)
                client.user_unfollow(290023231) #Real Madrid
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 290023231...")
                sleep(2)
                client.user_unfollow(1269788896) #Champions League
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 1269788896...")
                sleep(2)
                client.user_unfollow(29394004) #Chris Brown
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 29394004...")
                sleep(2)
                client.user_unfollow(11830955) #Taylor Swift
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 11830955...")
                sleep(2)
                client.user_unfollow(6380930) #Kendall Jenner
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 6380930...")
                sleep(2)
                client.user_unfollow(2094200507) #Virat Kohli
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 2094200507...")
                sleep(2)
                client.user_unfollow(9777455) #Zendaya
                unfollow += 1
                print(f"{YELLOW}[+] Unfollowing 9777455...")
                sleep(2)
            except KeyboardInterrupt:
                break
            print(f"{GREEN}[✓] Successfully followed: {follow} users")
            sleep(2)
            print(f"{GREEN}[✓] Successfully unfollowed: {unfollow} users")
            sleep(2)
            if follow - unfollow != 0:
                print(f"{RED}[✕] Failed to unfollow: {abs(follow - unfollow)} users")
            pers = (follow + unfollow) // 74
            print(f"{GREEN}[+] Percentage of success: {pers}%")
            sleep(1)
            print(f"{RED}[+] Percentage of fail: {100 - pers}%")
            sleep(1)
            if ga:
                followers_af = profile.followers
                print(f"{GREEN}[✓] Successfully added: {followers_af - followers_bef} followers.")
                sleep(1)
            if check:
                print(f"{RED}[!] WARNING: The data provided may be incorrect if your account is private and you haven't approved the follow requests")
                sleep(3)
                L = [user for user in FOLLOWERS]
                if L == FOLLOWERS:
                    print(f"{RED}[!] No new followers added ! Try checking the pending follow requests and try again.")
                else:
                    ADDS = [user for user in L if user not in FOLLOWERS]
                    for i, username in enumerate(ADDS):
                        print(f"{YELLOW}[+] User No{i+1} >>> {username}")
                sleep(2)
            if keep:
                name = 'log.txt'
                with open(name, 'w', encoding='utf8') as f:
                    f.write("\n"+"-"*40)
                    f.write(f"[+] Date: {datetime.now()}\n")
                    f.write(f"[+] Followed: {follow} users\n")
                    f.write(f"[+] Unfollowed: {unfollow} users"+"\n")
                    pers = (follow + unfollow) // 74
                    f.write(f"[+] Percentage of success: {pers}%\n")
                    f.write(f"[+] Percentage of fail: {100 - pers}%\n")
                    if ga:
                        followers_af = profile.followers
                        f.write(f"[✓] Successfully added: {followers_af - followers_bef} followers.\n")
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] File name >>> {name}")
                    print(f"{GREEN}[↪] Path >>> {fpath(name)}")
                    print(f"{GREEN}[↪] File size >>> {os.stat(fpath(name)).st_size} bytes")
                    sleep(4)
    elif option == 2:
        clear()
        ScriptInfo()
        sleep(4)
        print("\n\n")
    elif option == 3:
        clear()
        name = 'log.txt'
        if fpath(name):
            f = open(name,"w")
            f.close()
            print(f"{GREEN}[✓] Successfully cleared log !")
            sleep(1)
            print(f"{GREEN}[↪] File name >>> {name}")
            print(f"{GREEN}[↪] Location >>> {fpath(name)}")
            print(f"{GREEN}[↪] Size: 0 bytes")
            sleep(3)
        else:
            clear()
            print(f"{RED}[✕] Log file not found on this device !")
            sleep(2)
            print(f"{YELLOW}[+] Searched log file using name: {name}")
            sleep(2)
            print(f"{GREEN}[*] Please first create the log file and then use this option 😀")
            sleep(2)
            print(f"""{YELLOW}[+] Instructions: 
            1) Return to menu and enter the option number 1
            2) Enter <True> in the keep log question
            """)
            sleep(3)
    elif option == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using IGFI 😁")
        sleep(2)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using IGFI 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    valErr = num in [1,2]
    while not valErr:
        try:
            print(f"{YELLOW}[1] Return to menu")
            print(f"{YELLOW}[2] Exit")
            num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
            valErr = num in [1,2]
        except ValueError:
            print(f"{RED}[!] Please enter a valid number.")
            sleep(1)
            print(f"{GREEN}[+] Acceptable numbers: [1,2]")
            sleep(1)
    if num == 1:
        clear()
        main()
    else:
        clear()
        print(f"{RED}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
