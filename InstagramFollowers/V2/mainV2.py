"""
Author: new92
Github: @new92
InstaFollowV2: Script for increasing the followers of an Instagram account

*********IMPORTANT*********

User's login credentials (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's Instagram account
***************************
"""

try:
    import sys
    import platform
    from os import system
    from time import sleep
    import os
    import instagrapi
    import requests
    from instagrapi import *
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
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
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

def ProgInfo():
    author = 'new92'
    license1 = 'MIT'
    lang = 'es-US'
    language = 'Python'
    name = 'InstaFollowV2'
    api = None
    lines = 270
    f = '/IGFollowersIncreaser/InstagramFollowers/V2/mainV2.py'
    ptf = os.path.abspath(f)
    if os.path.exists(ptf):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 14
    forks = 10
    print("[+] Author: "+str(author))
    print("[+] Github: @"+str(author))
    print("[+] License: "+str(license1))
    print("[+] Natural language: "+str(lang))
    print("[+] Programming language(s) used: "+str(language))
    print("[+] Number of lines: "+str(lines))
    print("[+] Program's name: "+str(name))
    print("[+] API(s) used: "+str(api))
    print("[+] File size: "+str(fsize)+" bytes")
    print("[+] Github repo stars: "+str(stars))
    print("[+] Github repo forks: "+str(forks))


def banner():
  return """
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║╚════██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝░░███╔═╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░██╔══╝░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
"""

def nums():
    print("[1] Increase followers")
    print("[2] Show program info and exit")
    print("[3] Uninstall script")
    print("[4] Exit")

def main():
    print(banner())
    print("\n")
    print("[+] Script for increasing the followers of an account on Instagram (works for both public and private accounts)")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    nums()
    print("\n")
    option=int(input("[::] Please enter a number of the option (from above): "))
    while option < 1 or option > 4 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again the number: "))
    if option == 1:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print("[+] The login credentials will not be stored or saved")
        sleep(2)
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        username=str(input("[::] Please enter your username: "))
        while username == None or len(username) > 30:
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        resp = requests.get(f"https://www.instagram.com/{username}/")
        while resp.status_code == 404 or resp.status_code == 400:
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3 or opt == None:
                print("[!] Invalid number !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input("[::] Please enter the username: "))
                while username == None or len(username) > 30:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                main()
            else:
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! ☺️")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                exit(0)
        username=username.lower()
        username=username.strip()
        sleep(1)
        password=str(input("[::] Please enter your password: "))
        while password == None:
            print("[!] Invalid password !")
            sleep(1)
            password=str(input("[::] Please enter again your password: "))
        password=password.strip()
        sleep(1)
        print("|"+"-"*45+"|")
        clnt=instagrapi.Client()
        try:
            login = clnt.login(username,password)
            if login:
                print("[!] Login successful !")
                sleep(2)
                print("[+] Please wait while the program is increasing your followers...")
            else:
                print("[!] Login unsuccessful !")
                sleep(2)
                print("[+] Please check the username and/or the password !")
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input(">>> "))
                while num < 1 or num > 2 or num == None:
                    print("[!] Invalid number !")
                    sleep(1)
                    num=int(input(">>> "))
                if num == 1:
                    main()
                else:
                    if platform.system() == 'Windows':
                        system("cls")
                    else:
                        system("clear")
                    print("[+] Thank you for using my script 😁")
                    sleep(2)
                    print("[+] See you next time 👋")
                    sleep(1)
                    exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)
        sleep(2)
        print("[+] To end the process enter Ctrl + C")
        sleep(2)
        temp = True
        FOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455','204633036','176618189','1418652011','3439002676','212742998','528817151','13460080']
        NAMES = ['Cristiano Ronaldo','Cardi B','Kim Kardashian','Ariana Grande','Nicki Minaj','Beyonce','Katy Perry','Selena Gomez','Justin Bieber','Lionel Messi','Neymar Jr','Kylian Mbappe','Dua Lipa','Billie Eilish','Kylie Jenner','Khloe Kardashian','Kourtney Kardashian','Jennifer Lopez','Shakira','NBA','Instagram','National Geographic','FC Barcelona','Real Madrid','Champions League','Chris Brown','Taylor Swift','Kendall Jenner','Virat Kohli','Zendaya','Marvel','Tom Holland','Emma Watson','Millie Bobby Brown','Shawn Mendes','NASA','Nike']
        print("[!] NOTE: Use this program every 2 days in order for your account not to get blocked")
        sleep(5)
        while temp:
            for i in range(len(FOLLOW)-1):
                try:
                    clnt.user_follow(FOLLOW[i])
                except Exception as key:
                    print("[!] Error !")
                    sleep(1)
                    print(key)
                    sleep(1)
                    print("[+] Exiting...")
                    quit(0)
                print(f"[+] Following {NAMES[i]}...")
                sleep(3)
                print(f"[+] Next user to follow: {NAMES[i+1]}")
                sleep(1)
            for i in range(len(FOLLOW)-1):
                try:
                    clnt.user_unfollow(FOLLOW[i])
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(1)
                    print("[+] Exiting...")
                    quit(0)
                print(f"[+] Unfollowing {NAMES[i]}...")
                sleep(3)
                print(f"[+] Next user to unfollow: {NAMES[i+1]}")
                sleep(1)
    elif option == 2:
        ProgInfo()
    elif option == 3:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
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
        dir = os.path.abspath('IGFollowersIncreaser')
        rmdir(dir)
        print("[+] Files and dependencies uninstalled successfully !")
    else:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        exit(0)

if __name__ == '__main__':
    main()
