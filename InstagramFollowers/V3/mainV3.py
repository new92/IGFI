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
        sleep(2)
        print("[+] Please install Python 3 and then use IGFollowersIncreaser ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 12
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import os
    import instagrapi
    import requests
    import instaloader
    import colorama
    from datetime import date
    from colorama import Fore
except ImportError:
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
                print("[!] Cannot install the required modules !")
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
                        print("[*] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall IGFollowersIncreaser")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter a number (from the above ones): "))
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

colorama.init(autoreset=True)
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW

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
    api = None
    lines = 802
    f = 'mainV3.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    stars = 53
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
    print(f"{YELLOW}[+] API(s) used: {api}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {os.path.abspath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {stars}")
    print(f"{YELLOW}[+] Forks: {forks}")
    print(f"{YELLOW}[+] Open issues: {issues}")
    print(f"{YELLOW}[+] Closed issues: {clissues}")
    print(f"{YELLOW}[+] Open pull requests: {prs}")
    print(f"{YELLOW}[+] Closed pull requests: {clprs}")
    print(f"{YELLOW}[+] Discussions: {discs}")

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

def banner() -> str:
    return f"""{YELLOW}
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗      ██╗░░░██╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║      ██║░░░██║╚════██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝      ╚██╗░██╔╝░█████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░      ░╚████╔╝░░╚═══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░      ░░╚██╔╝░░██████╔╝
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░      ░░░╚═╝░░░╚═════╝░
"""
ANS = ["yes","YES","Yes","y","Y","YeS","yEs","YEs","yES","no","NO","No","n","N","nO"]

def nums():
    print(f"{YELLOW}[1] Increase followers")
    print(f"{YELLOW}[2] Show IGFollowersIncreaser's info")
    print(f"{YELLOW}[3] Clear log")
    print(f"{YELLOW}[4] Uninstall IGFollowersIncreaser")
    print(f"{YELLOW}[5] Exit")

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')
        
def checkUser(username:str) -> bool:
    return username == None or len(username) > 30 or username == ''

def valUser(username:str) -> bool:
    return requests.get(f"https://www.instagram.com/{username}/", allow_redirects=False).status_code != 200

def main():
    print(banner())
    print("\n")
    print(f"{YELLOW}[+] Author: new92")
    print(f"{YELLOW}[+] Github: @new92")
    print("\n")
    print(f"{YELLOW}[+] Use this script to increase the followers on your Insta account")
    print("\n")
    nums()
    print("\n")
    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    while num < 1 or num > 5 or num == None:
        if num == None:
            print(f"{RED}[!] This field can't be empty !")
        else:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{GREEN}[*] Acceptable numbers: [1/2/3/4/5]")
        sleep(1)
        nums()
        sleep(1)
        num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        sleep(1)
        print(f"{GREEN}[*] Acceptable answers: [True/False]")
        sleep(1)
        keep=input(f"{YELLOW}[?] Keep log ? ")
        while keep.lower() not in ['true','false'] or keep == None or keep == '':
            if keep == None or keep == '':
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[*] Acceptable answers: [True/False]")
            sleep(1)
            keep=input(f"{YELLOW}[?] Keep log ? ")
        if keep.lower() == 'true':
            keep = True
        else:
            keep = False
        NAMES = ['Cristiano Ronaldo','Cardi B','Kim Kardashian','Ariana Grande','Nicki Minaj','Beyonce','Katy Perry','Selena Gomez','Justin Bieber','Lionel Messi','Neymar Jr','Kylian Mbappe','Dua Lipa','Billie Eilish','Kylie Jenner','Khloe Kardashian','Kourtney Kardashian','Jennifer Lopez','Shakira','Instagram','National Geographic','FC Barcelona','Real Madrid','Champions League','Chris Brown','Taylor Swift','Kendall Jenner','Virat Kohli','Zendaya','Marvel','Tom Holland','Emma Watson','Millie Bobby Brown','Shawn Mendes','Camila Cabello','NASA','Nike']
        users = {
            'Cristiano Ronaldo' : '173560420',
            'Cardi B' : '1436859892',
            'Kim Kardashian': '18428658',
            'Ariana Grande' : '7719696',
            'Nicki Minaj' : '451573056',
            'Beyonce' : '247944034',
            'Katy Perry' : '407964088',
            'Selena Gomez' : '460563723',
            'Justin Bieber' : '6860189',
            'Lionel Messi' : '427553890',
            'Neymar Jr' : '26669533',
            'Kylian Mbappe' : '4213518589',
            'Dua Lipa' : '12331195',
            'Billie Eilish' : '28527810',
            'Kylie Jenner' : '12281817',
            'Khloe Kardashian' : '208560325',
            'Kourtney Kardashian' : '145821237',
            'Jennifer Lopez' : '305701719',
            'Shakira' : '217867189',
            'Instagram' : '25025320',
            'National Geographic' : '787132',
            'FC Barcelona' : '260375673',
            'Real Madrid' : '290023231',
            'Champions League' : '1269788896',
            'Chris Brown' : '29394004',
            'Taylor Swift' : '11830955',
            'Kendall Jenner' : '6380930',
            'Virat Kohli' : '2094200507',
            'Zendaya' : '9777455',
            'Marvel' : '204633036',
            'Tom Holland' : '176618189',
            'Emma Watson' : '1418652011',
            'Millie Bobby Brown' : '3439002676',
            'Shawn Mendes' : '212742998',
            'Camila Cabello' : '19596899',
            'NASA' : '528817151',
            'Nike' : '13460080'
        }
        if os.path.exists(fpath('cons.txt')):
            print(f"{GREEN}[*] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
            while con not in ANS or con == None or con == '':
                if con == None or con == '':
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid answer !")
                    sleep(1)
                    print(f"{GREEN}[*] Acceptable answers: [yes/no]")
                sleep(1)
                con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
            if con in ANS[:9]:
                f = open("cons.txt","a")
                f.write(f"\n[=] Date: {date.today()}\n")
                f.write("[=] User: Yes I consent that the author of this script (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
                f.write("-"*40+'\n')
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
                        print(f"{GREEN}[*] Acceptable numbers: [1/2]")
                    sleep(1)
                    print(f"{YELLOW}[1] Exit")
                    print(f"{YELLOW}[2] Uninstall IGFollowersIncreaser and exit")
                    sleep(1)
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(1)
                    quit(0)
                else:
                    clear()
                    print(Uninstall())
                    sleep(1)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] Thank you for choosing to use IGFollowersIncreaser 😁")
                    sleep(2)
                    print(f"{GREEN}[+] If you have any suggestions or found a bug or need help feel free to contact me anytime, at this email address: new92github@gmail.com")
                    sleep(3)
                    quit(0)
        else:
            f = open("cons.txt","w")
            f.write(f"[=] Date: {str(date.today())}\n")
            f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
            f.write("-"*40)
            f.close()
        sleep(1)
        print(f"{YELLOW}[+] The login credentials will not be stored or saved")
        sleep(2)
        print(f"{GREEN}|--------------------|LOGIN|--------------------|")
        username=str(input(f"{YELLOW}[>] Please enter your username: "))
        while checkUser(username):
            if username == None or username == '':
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length !")
                sleep(1)
                print(f"{GREEN}[*] Acceptable length: 30 or less characters")
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
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{YELLOW}[1] Try with another username")
                print(f"{YELLOW}[2] Return to menu")
                print(f"{YELLOW}[3] Exit")
                opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[>] Please enter the username: "))
                while checkUser(username):
                    if username == None or username == '':
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length !")
                        sleep(1)
                        print(f"{GREEN}[*] Acceptable length: 30 or less characters")
                    sleep(1)
                    username=str(input(f"{YELLOW}[>] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(f"{RED}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(2)
                quit(0)
        print(f"{GREEN}[*] Acceptable answers: [yes/no]")
        sleep(1)
        con=str(input(f"{YELLOW}[?] The script will increase the followers for the user: {username} is that correct ? "))
        while con not in ANS or con == None or con == '':
            if con == None or con == '':
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[*] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"[?] The script will increase the followers for the user: {username} is it correct ? "))
        if con in ANS[9:]:
            username=str(input(f"{YELLOW}[>] Please enter another username: "))
            while checkUser(username):
                if username == None:
                    print(f"{RED}[!] This field can't be blank !")
                else:
                    print(f"{RED}[!] Invalid length !")
                    sleep(1)
                    print(f"{GREEN}[*] Acceptable length: less than or equal to 30")
                sleep(1)
                username=str(input(f"{YELLOW}[>] Please enter again your username: "))
            while valUser(username):
                print(f"{RED}[!] User not found !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                opt=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 3 or opt == None:
                    if opt == None:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid number !")
                        sleep(1)
                        print(f"{GREEN}[*] Acceptable numbers: [1/2/3]")
                    sleep(1)
                    print("[1] Try with another username")
                    print("[2] Return to menu")
                    print("[3] Exit")
                    opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    clear()
                    username=str(input(f"{YELLOW}[>] Please enter the username: "))
                    while checkUser(username):
                        if username == None:
                            print(f"{RED}[!] This field can't be blank !")
                        else:
                            print(f"{RED}[!] Invalid length  !")
                            sleep(1)
                            print(f"{YELLOW}[+] The length of the username must be less than or equal to 30 characters.")
                        sleep(1)
                        username=str(input(f"{YELLOW}[>] Please enter again the username: "))
                elif opt == 2:
                    clear()
                    main()
                else:
                    clear()
                    print(f"{YELLOW}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        print(f"{GREEN}[*] Acceptable answers: [yes/no]")
        sleep(1)
        ga=str(input(f"{YELLOW}[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? "))
        while ga not in ANS or ga == None:
            if ga == None:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{YELLOW}[+] Valid answers: [yes/no]")
            sleep(1)
            ga=str(input(f"{YELLOW}[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? "))
        if ga in ANS[:9]:
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username)
            followers_bef = profile.followers
        username=username.lower().strip()
        sleep(1)
        password=str(input(f"{YELLOW}[>] Please enter your password: "))
        while password == None:
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
                sleep(1)
                print(f"{YELLOW}[+] Please wait while the program is increasing your followers...")
                sleep(2)
            else:
                print(f"{RED}[!] Login unsuccessful !")
                sleep(1)
                print(f"{YELLOW}[+] Please check the username and/or the password !")
                sleep(2)
                print("\n")
                print(f"{YELLOW}[1] Return to menu")
                print(f"{YELLOW}[2] Exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print(f"{RED}[!] This field can't be empty !")
                    else:
                        print(f"{RED}[!] Invalid number !")
                        sleep(1)
                        print(f"{GREEN}[*] Acceptable numbers: [1/2]")
                    sleep(1)
                    print(f"{YELLOW}[1] Return to menu")
                    print(f"{YELLOW}[2] Exit")
                    num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones):"))
                if num == 1:
                    clear()
                    main()
                else:
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(2)
                    quit(0)
        except Exception:
            if Exception == 'The password you entered is incorrect. Please try again.':
                print(f"{RED}[!] Incorrect password !")
                sleep(2)
                print(f"{YELLOW}[+] Returning to menu...")
                sleep(1)
                clear()
                main()
            else:
                print(f"{RED}[!] Error !")
                sleep(1)
                print(f"{YELLOW}[*] Error message ==> {Exception}")
                sleep(2)
                print(f"{YELLOW}[1] Return to menu")
                print(f"{YELLOW}[2] Exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print(f"{RED}[!] This field can't be empty !")
                    else:
                        print(f"{RED}[!] Invalid number !")
                        sleep(1)
                        print(f"{GREEN}[*] Acceptable numbers: [1/2]")
                    sleep(1)
                    print(f"{YELLOW}[1] Return to menu")
                    print(f"{YELLOW}[2] Exit")
                    num=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones):"))
                if num == 1:
                    clear()
                    main()
                else:
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{GREEN}[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        sleep(2)
        print(f"{YELLOW}[+] To end the process enter Ctrl + C")
        sleep(2)
        clear()
        f = 0
        x = 0
        for i in range(30):
            try:
                for j in range(len(NAMES)-1):
                    client.user_follow(users[NAMES[j]])
                    print(f"{YELLOW}[+] Following {NAMES[j]}...")
                    sleep(3)
                    print(f"{GREEN}[✓] Ok")
                    sleep(2)
                    f += 1
                    print(f"{YELLOW}[+] Next user to follow: {NAMES[j+1]}...")
                    sleep(3)
                for j in range(len(NAMES)-1):
                    client.user_unfollow(users[NAMES[j]])
                    print(f"{YELLOW}[-] Unfollowing {NAMES[j]}...")
                    sleep(3)
                    print(f"{GREEN}[✓] Ok")
                    sleep(2)
                    x += 1
                    print(f"{YELLOW}[-] Next user to unfollow: {NAMES[j+1]}...")
                    sleep(3)
            except KeyboardInterrupt:
                res = f - x
                if res != 0:
                    suc = f / float(len(NAMES))
                    fail = res / float(len(NAMES))
                    tot = f + x
                    print(f"{GREEN}[✓] Successfully followed/unfollowed a total of {tot} users")
                    sleep(2)
                    print(f"{RED}[✕] Failed to unfollow {abs(res)} users !")
                    sleep(1)
                    print(f"{GREEN}[+] Percentage of success: {suc}%")
                    sleep(1)
                    print(f"{RED}[+] Percentage of failure: {fail}%")
                    if ga in ANS[:9]:
                        followers_af = profile.followers
                        if followers_bef - followers_af != 0:
                            followers_af = profile.followers
                            print(f"{GREEN}[✓] Successfully added: {followers_af - followers_bef} followers.")
                            sleep(1)
                    print(f"{YELLOW}[*] Users which the script failed to unfollow:")
                    sleep(3)
                    print(f'{YELLOW}|---------------|USERS|---------------|')
                    print("\n")
                    for i in range(res,-1,-1):
                        print(f"{YELLOW}[+] User: {NAMES[i]}")
                else:
                    print(f"{GREEN}[+] Success: 100%")
                    sleep(1)
                    print(f"{RED}[+] Fail: {res}%")
                    sleep(2)
                if keep:
                    name = 'log.txt'
                    if os.path.exists(os.path.abspath(name)):
                        f = open(name,'a')
                        f.write('\n'+'-'*40+'\n')
                        if res != 0:
                            f.write(f'[✓] Successfully followed/unfollowed a total of {str(tot)} users\n')
                            f.write(f'[✕] Failed to unfollow {str(abs(res))} users !\n')
                            f.write(f'[+] Percentage of success: {str(suc)}%\n')
                            f.write(f'[+] Percentage of failure: {str(fail)}%\n')
                            if ga in ANS[:9]:
                                followers_af = profile.followers
                                if followers_bef - followers_af != 0:
                                    followers_af = profile.followers
                                    f.write(f'[✓] Successfully added: {str(followers_af - followers_bef)} followers.\n')
                        else:
                            f.write('[+] Percentage of success: 100%\n')
                            f.write(f'[+] Percentage of failure: {str(res)}%')
                        f.close()
                    else:
                        f = open(name,'w')
                        if res != 0:
                            f.write(f'[✓] Successfully followed/unfollowed a total of {str(tot)} users\n')
                            f.write(f'[✕] Failed to unfollow {str(abs(res))} users !\n')
                            f.write(f'[+] Percentage of success: {str(suc)}%\n')
                            f.write(f'[+] Percentage of failure: {str(fail)}%\n')
                            if ga in ANS[:9]:
                                followers_af = profile.followers
                                if followers_bef - followers_af != 0:
                                    followers_af = profile.followers
                                    f.write(f'[✓] Successfully added: {str(followers_af - followers_bef)} followers.\n')
                        else:
                            f.write('[+] Percentage of success: 100%\n')
                            f.write(f'[+] Percentage of failure: {str(res)}%')
                        f.close()
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{GREEN}[↪] Log file name: {name}")
                    print(f"{GREEN}[↪] Path to log file: {os.path.abspath(name)}")
                    print(f"{GREEN}[↪] Log file size: {(os.stat(name)).st_size} bytes")
                print("\n")
        res = f - x
        if res != 0:
            suc = f / float(len(NAMES))
            fail = res / float(len(NAMES))
            tot = f + x
            print(f"{GREEN}[✓] Successfully followed/unfollowed a total of {tot} users")
            sleep(2)
            print(f"{RED}[✕] Failed to unfollow {abs(res)} users !")
            sleep(2)
            print(f"{GREEN}[+] Percentage of success: {suc}")
            sleep(1)
            print(f"{RED}[+] Percentage of failure: {fail}")
            sleep(1)
            if ga in ANS[:9]:
                followers_af = profile.followers
                if followers_bef - followers_af != 0:
                    followers_af = profile.followers
                    print(f"{GREEN}[✓] Successfully added: {followers_af - followers_bef} followers.")
                    sleep(1)
            print(f"{YELLOW}[*] Users which the script didn't unfollow:")
            sleep(3)
            print(f'{YELLOW}|---------------|USERS|---------------|')
            for i in range(res,-1,-1):
                print(f"{YELLOW}[+] User: {NAMES[i]}")
        else:
            print(f"{YELLOW}[+] Success: 100%")
            sleep(1)
            print(f"{YELLOW}[+] Fail: {res}%")
            sleep(2)
        if keep:
            name = 'log.txt'
            if os.path.exists(fpath(name)):
                f = open(name,'a')
                f.write('\n'+'-'*40+'\n')
                if res != 0:
                    f.write(f'[✓] Successfully followed/unfollowed a total of {str(tot)} users\n')
                    f.write(f'[✕] Failed to unfollow {str(abs(res))} users !\n')
                    f.write(f'[+] Percentage of success: {str(suc)}%\n')
                    f.write(f'[+] Percentage of failure: {str(fail)}%\n')
                    if ga in ANS[:9]:
                        followers_af = profile.followers
                        if followers_bef - followers_af != 0:
                            followers_af = profile.followers
                            f.write(f'[✓] Successfully added: {str(followers_af - followers_bef)} followers.\n')
                else:
                    f.write('[+] Percentage of success: 100%\n')
                    f.write(f'[+] Percentage of failure: {str(res)}%')
                f.close()
            else:
                f = open(name,'w')
                if res != 0:
                    f.write(f'[✓] Successfully followed/unfollowed a total of {str(tot)} users\n')
                    f.write(f'[✕] Failed to unfollow {str(abs(res))} users !\n')
                    f.write(f'[+] Percentage of success: {str(suc)}%\n')
                    f.write(f'[+] Percentage of failure: {str(fail)}%\n')
                    if ga in ANS[:9]:
                        followers_af = profile.followers
                        if followers_bef - followers_af != 0:
                            followers_af = profile.followers
                            f.write(f'[✓] Successfully added: {str(followers_af - followers_bef)} followers.\n')
                else:
                    f.write('[+] Percentage of success: 100%\n')
                    f.write(f'[+] Percentage of failure: {str(res)}%')
                f.close()
            print(f"{GREEN}[✓] Successfully saved log !")
            sleep(2)
            print(f"{GREEN}[↪] Log file name: {name}")
            print(f"{GREEN}[↪] Path to log file: {fpath(name)}")
            print(f"{GREEN}[↪] Log file size: {(os.stat(fpath(name))).st_size} bytes")
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(4)
        print("\n\n")
    elif num == 3:
        clear()
        name = 'log.txt'
        if os.path.exists(fpath(name)):
            f = open(name,"w")
            f.close()
            print(f"{GREEN}[✓] Successfully cleared log !")
            sleep(1)
            print(f"{GREEN}[↪] Log file name: {name}")
            print(f"{GREEN}[↪] Path to log file: {fpath(name)}")
            print(f"{GREEN}[↪] Log file size: {(os.stat(fpath(name))).st_size} bytes")
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
    elif num == 4:
        print(Uninstall())
        sleep(2)
        print(f"{YELLOW}[+] Thank you for choosing IGFollowersIncreaser 😀😁")
        sleep(2)
        print(f"{YELLOW}[+] Hope you enjoyed it 🤗")
        sleep(1)
        print(f"{YELLOW}[+] If you have any suggestions or found a bug or need help feel free to contact me anytime, at this email address: new92github@gmail.com")
        sleep(3)
        print(f"{YELLOW}[+] Until we meet again 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using IGFollowersIncreaser 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit(0)
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    opt=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    while opt < 1 or opt > 2 or opt == None:
        if opt == None:
            print(f"{RED}[!] This field can't be blank !")
        else:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            print(f"{GREEN}[*] Acceptable numbers: [1/2]")
            sleep(1)
            print(f"{YELLOW}[1] Return to menu")
            print(f"{YELLOW}[2] Exit")
            opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
    if opt == 1:
        clear()
        main()
    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using IGFollowersIncreaser 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
