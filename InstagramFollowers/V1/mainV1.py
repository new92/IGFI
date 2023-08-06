# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

IGFollowersIncreaser: Use this script to increase the followers of an Insta account


*********IMPORTANT*********
User's login credentials (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's Instagram account
***************************
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! IGFollowersIncreaser requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IGFollowersIncreaser ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 10
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import instagrapi
    import requests
    import os
    import instaloader
    from datetime import date
    from colorama import init, Fore
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in IGFollowersIncreaser have been installed !")
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
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
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
                    rmdir(fpath('IGFollowersIncreaser'))
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

print(f"{GREEN}[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    author = 'new92'
    lice = 'MIT'
    lang = 'en-US'
    language = 'Python'
    name = 'IGFollowersIncreaser'
    lines = 828
    f = 'mainV1.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    stars = 56
    forks = 31
    issues = 1
    clissues = 5
    prs = 0
    clprs = 8
    discs = 5
    print(f"{YELLOW}[+] Author: {author}")
    print(f"{YELLOW}[+] Github: @{author}")
    print(f"{YELLOW}[+] License: {lice}")
    print(f"{YELLOW}[+] Natural language: {lang}")
    print(f"{YELLOW}[+] Programming language(s) used: {language}")
    print(f"{YELLOW}[+] Number of lines: {lines}")
    print(f"{YELLOW}[+] Script's name: {name}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {fpath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {stars}")
    print(f"{YELLOW}[+] Forks: {forks}")
    print(f"{YELLOW}[+] Open issues: {issues}")
    print(f"{YELLOW}[+] Closed issues: {clissues}")
    print(f"{YELLOW}[+] Open pull requests: {prs}")
    print(f"{YELLOW}[+] Closed pull requests: {clprs}")
    print(f"{YELLOW}[+] Discussions: {discs}")

def banner() -> str:
    return f"""{YELLOW}
    ██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗░░███╗░░
    ██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║░████║░░
    ██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝██╔██║░░
    ██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░╚═╝██║░░
    ██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
    ╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
    """

ANS = ["yes","no"]

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
    rmdir(fpath('IGFollowersIncreaser'))
    return f"{GREEN}[✓] Files and dependencies uninstalled successfully !"

def checkUser(username:str) -> bool:
    return username == None or len(username) > 30 or username == '' or username == ' '

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def nums():
    print(f"{YELLOW}[1] Increase followers")
    print(f"{YELLOW}[2] Show IGFollowersIncreaser's info")
    print(f"{YELLOW}[3] Clear log")
    print(f"{YELLOW}[4] Uninstall IGFollowersIncreaser")
    print(f"{YELLOW}[5] Exit")

def main():
    print(banner())
    print("\n")
    print(f"{YELLOW}[+] IGFollowersIncreaser is a tool which helps the increment of the followers of a user on Instagram")
    print("\n")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print("\n")
    nums()
    print("\n")
    option=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    while option < 1 or option > 5 or option == None:
        if option == None:
            print(f"{RED}[!] This field can't be blank !")
        else:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{YELLOW}[+] Acceptable numbers: [1/2/3/4/5]")
        sleep(1)
        nums()
        option=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
    if option == 1:
        clear()
        sleep(1)
        print(f"{YELLOW}[+] Acceptable answers: [yes/no]")
        sleep(1)
        keep=str(input(f"{YELLOW}[?] Keep log ? "))
        while keep.lower() not in ANS or keep == None or keep == '' or keep == ' ':
            if keep == '' or keep == ' ' or keep == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            keep=str(input(f"{YELLOW}[?] Keep log ? "))
        keep = True if keep.lower() == ANS[0] else False
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1)
        check=str(input("[?] Display the usernames of the followers added ? "))
        while check.lower() not in ANS or check == None or check == '' or check == ' ':
            if check == None or check == '' or check == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            check=str(input("[?] Display the usernames of the followers added ? "))
        check = True if check.lower() == ANS[0] else False
        if os.path.exists(fpath('cons.txt')):
            print(f"{YELLOW}[+] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
            while con.lower() not in ANS or con == None or con == '' or con == ' ':
                if con == None or con == '' or con == ' ':
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid answer !")
                    sleep(1)
                    print(f"{YELLOW}[+] Acceptable answers: [yes/no]")
                sleep(1)
                con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
            if con.lower() == ANS[0]:
                f = open("cons.txt","a")
                f.write(f"\n[=] Date: {date.today()}\n")
                f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
                f.write("-"*40)
                f.close()
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall IGFollowersIncreaser and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid number !")
                        sleep(1)
                        print(f"{YELLOW}[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print(f"{YELLOW}[1] Exit")
                    print(f"{YELLOW}[2] Uninstall IGFollowersIncreaser and exit")
                    sleep(1)
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
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
                    print(f"{YELLOW}[+] Thank you for using IGFollowersIncreaser 🫡")
                    sleep(2)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(1)
                    quit(0)
        else:
            f = open("cons.txt","w")
            f.write(f"[=] Date: {date.today()}\n")
            f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
            f.write("-"*40+'\n')
            f.close()
        print("\n")
        print(f"{YELLOW}[+] The login credentials will not be stored or saved")
        sleep(2)
        print(f"{GREEN}|--------------------|LOGIN|--------------------|")
        username=str(input(f"{YELLOW}[>] Please enter your username: "))
        username = username.lower().strip()
        while checkUser(username):
            if username == None or username == '':
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
            while opt < 1 or opt > 3 or opt == None:
                if opt == None:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1/2/3]")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                username=str(input(f"{YELLOW}[>] Please enter the username: "))
                username = username.lower().strip()
                while checkUser(username):
                    if username == None or username == '':
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
                print(f"{YELLOW}[+] Thank you for using IGFollowersIncreaser 😁")
                sleep(2)
                print(f"{YELLOW}[+] See you next time 👋")
                sleep(1)
                quit(0)
        print(f"{YELLOW}[+] Acceptable answers: [yes/no]")
        sleep(1)
        ga=str(input(f"{YELLOW}[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? "))
        while ga.lower() not in ANS or ga == None or ga == '' or ga == ' ':
            if ga == None or ga == '' or ga == ' ':
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
            profile = instaloader.Profile.from_username(loader.context, username)
            followers_bef = profile.followers
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
        sleep(1)
        password=str(input(f"{YELLOW}[>] Please enter your password: "))
        while password == None or password == '' or password == ' ':
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
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid number !")
                        sleep(1)
                        print(f"{YELLOW}[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print(f"{YELLOW}[1] Return to menu")
                    print(f"{YELLOW}[2] Exit")
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
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
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid number !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(1)
                print(f"{YELLOW}[1] Return to menu")
                print(f"{YELLOW}[2] Exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
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
            pers = (follow + unfollow) / 74.0
            print(f"{GREEN}[+] Percentage of success: {pers}")
            sleep(1)
            print(f"{RED}[+] Percentage of fail: {float(100 - pers)}%")
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
                if os.path.exists(fpath(name)):
                    f = open(name,'a')
                    f.write('\n'+'-'*40+'\n')
                    f.write(f"[+] Date: {str(date.today())}\n")
                    f.write(f"[+] Followed: {str(follow)} users\n")
                    f.write(f"[+] Unfollowed: {str(unfollow)} users\n")
                    if follow - unfollow != 0:
                        f.write(f"[✕] Failed to unfollow: {str(abs(follow - unfollow))} users\n")
                    pers = (follow + unfollow) / 74.0
                    f.write(f"[+] Percentage of success: {str(pers)}%\n")
                    f.write(f"[+] Percentage of fail: {str(float(100 - pers))}%\n")
                    if ga:
                        followers_af = profile.followers
                        f.write(f"[✓] Successfully added: {str(followers_af - followers_bef)} followers.\n")
                    if check:
                        L = [user for user in FOLLOWERS]
                        if L != FOLLOWERS:
                            ADDS = [user for user in L if user not in FOLLOWERS]
                            for i, username in enumerate(ADDS):
                                f.write(f"[+] User No{str(i+1)} >>> {username}\n")
                    f.close()
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] Log file name: {name}")
                    print(f"{GREEN}[↪] Path to log file: {fpath(name)}")
                    print(f"{GREEN}[↪] Log file size: {os.stat(fpath(name)).st_size} bytes")
                    sleep(4)
                else:
                    f = open(name,"w")
                    f.write("\n"+"-"*40)
                    f.write(f"[+] Date: {date.today()}\n")
                    f.write(f"[+] Followed: {str(follow)} users\n")
                    f.write(f"[+] Unfollowed: {str(unfollow)} users"+"\n")
                    pers = (follow + unfollow) / 74.0
                    f.write(f"[+] Percentage of success: {str(pers)}%\n")
                    f.write(f"[+] Percentage of fail: {str(float(100 - pers))}%\n")
                    if ga:
                        followers_af = profile.followers
                        f.write(f"[✓] Successfully added: {str(followers_af - followers_bef)} followers.\n")
                    f.close()
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] Log file name: {name}")
                    print(f"{GREEN}[↪] Path to log file: {fpath(name)}")
                    print(f"{GREEN}[↪] Log file size: {os.stat(fpath(name)).st_size} bytes")
                    sleep(4)
    elif option == 2:
        clear()
        ScriptInfo()
        sleep(4)
        print("\n\n")
    elif option == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using IGFollowersIncreaser 😁")
        sleep(2)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using IGFollowersIncreaser 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    while num < 1 or num > 2 or num == None:
        if num == None:
            print(f"{RED}[!] This field can't be empty !")
        else:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{GREEN}[+] Acceptable numbers: [1/2]")
        sleep(1)
        print(f"{YELLOW}[1] Return to menu")
        print(f"{YELLOW}[2] Exit")
        num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
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
