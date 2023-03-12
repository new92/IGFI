# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
InstaFollowV1: Script for increasing the followers of an Instagram account


*********IMPORTANT*********
User's login credentials (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's Instagram account
***************************
"""
try:
    import sys
    if sys.version_info[0] < 3:
        print("[!] Error ! This script requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(2)
        print("[+] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from os import system
    from time import sleep
    import instagrapi
    import os
    import requests
    import instaloader
    from datetime import date
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this script have been installed !")
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
                print("[*] Error message ==> "+str(ex))
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
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
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
                    rmdir(os.path.abspath('IGFollowersIncreaser'))
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
    
def ProgInfo():
    author = 'new92'
    lice = 'MIT'
    lang = 'es-US'
    language = 'Python'
    name = 'InstaFollowV1'
    lines = 843
    f = '/IGFollowersIncreaser/InstagramFollowers/V1/mainV1.py'
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 18
    forks = 12
    print(f"[+] Author: {author}")
    print(f"[+] Github: @{author}")
    print(f"[+] License: {lice}")
    print(f"[+] Natural language: {lang}")
    print(f"[+] Programming language(s) used: {language}")
    print(f"[+] Number of lines: {lines}")
    print(f"[+] Script's name: {name}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] Github repo stars: {stars}")
    print(f"[+] Github repo forks: {forks}")

def banner() -> str:
    return """
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗░░███╗░░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║░████║░░
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝██╔██║░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░╚═╝██║░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
"""

ANS = ["yes","YES","Yes","y","Y","YeS","yEs","YEs","yES","no","NO","No","n","N","nO"]

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
    rmdir(os.path.abspath('IGFollowersIncreaser'))
    return "[+] Files and dependencies uninstalled successfully !"

def checkUser(username:str) -> bool:
    return username == None or len(username) > 30

def clear():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

def nums():
    print("[1] Increase followers")
    print("[2] Show program info and exit")
    print("[3] Keep log")
    print("[4] Clear log")
    print("[5] Uninstall script")
    print("[6] Exit")

def main():
    print(banner())
    print("\n")
    print("[+] Script for increasing the followers of an Instagram account")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    nums()
    print("\n")
    option=int(input("[>] Please enter a number (from the above ones): "))
    while option < 1 or option > 6 or option == None:
        if option == None:
            print("[!] This field can't be blank !")
        else:
            print("[!] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1/2/3/4/5/6]")
        sleep(1)
        nums()
        option=int(input("[>] Please enter again a number (from the above ones): "))
    if option == 1:
        clear()
        sleep(1)
        if os.path.exists("cons.txt"):
            con=str(input("[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? [yes/no] "))
            if con in ANS[:9]:
                f = open("cons.txt","a")
                f.write("[=] Date: "+str(date.today())+"\n")
                f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.")
                f.write("-"*40)
                f.close()
            else:
                print("[OK]")
                sleep(1)
                print("[1] Exit")
                print("[2] Uninstall script and exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Exit")
                    print("[2] Uninstall script and exit")
                    sleep(1)
                    num=int(input("[>] Please enter a number (from the above ones): "))
                if num == 1:
                    print("[+] Exiting...")
                    sleep(1)
                    quit(0)
                else:
                    print(Uninstall())
                    sleep(2)
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] Thank you for using my script 🫡")
                    sleep(2)
                    print("[+] Until we meet again 👋")
                    sleep(1)
                    quit(0)
        else:
            f = open("cons.txt","w")
            f.write("[=] Date: "+str(date.today())+"\n")
            f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.")
            f.write("-"*40)
            f.close()
        print("\n")
        print("[+] The login credentials will not be stored or saved")
        sleep(2)
        print("|"+"-"*20+"login".upper()+"-"*20+"|")
        username=str(input("[>] Please enter your username: "))
        while checkUser(username):
            if username == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid length !")
                sleep(1)
                print("[+] The length of the username must be less than or equal to 30 characters.")
            sleep(1)
            username=str(input("[>] Please enter again your username: "))
        while requests.get(f"https://www.instagram.com/{username}/").status_code == 404 or requests.get(f"https://www.instagram.com/{username}/").status_code == 400:
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3 or opt == None:
                if opt == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2/3]")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                username=str(input("[>] Please enter the username: "))
                while checkUser(username):
                    if username == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid username !")
                        sleep(1)
                        print("[+] The length of the username must be lower than or equal to 30 characters.")
                    sleep(1)
                    username=str(input("[>] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        ga=str(input("[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? [yes/no] "))
        while ga not in ANS or ga == None:
            if ga == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Valid answers: [yes/no]")
            sleep(1)
            ga=str(input("[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? [yes/no] "))
        username=username.lower()
        username=username.strip()
        if ga in ANS[:9]:
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username)
            followers_bef = profile.followers
        sleep(1)
        password=str(input("[>] Please enter your password: "))
        while password == None or type(password) != str:
            if password == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Password must be a string !")
            sleep(1)
            password=str(input("[>] Please enter again your password: "))
        password=password.strip()
        sleep(1)
        print("|"+"-"*45+"|")
        client=instagrapi.Client()
        try:
            login = client.login(username,password)
            if login:
                print("[*] Login successful !")
                sleep(2)
                print("[+] Please wait while the program is increasing your followers...")
            else:
                print("[!] Login unsuccessful !")
                sleep(2)
                print("[+] Please check the username and/or the password !")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print("[!] This field can't be empty !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Return to menu")
                    print("[2] Exit")
                    num=int(input("[>] Please enter a number (from the above ones): "))
                if num == 1:
                    main()
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(f"[=] Error message -> {ex}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None:
                if num == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
            if num == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        sleep(2)
        clear()
        print("[+] To end the process enter Ctrl + C")
        sleep(2)
        print("[*] NOTE: Use this program every 2 days in order for your account not to get blocked")
        follow = 0
        unfollow = 0
        while True:
            try:
                client.user_follow(173560420) #Cristiano Ronaldo
                follow += 1
                print("[+] Following 173560420...")
                sleep(2)
                client.user_follow(1436859892) #Cardi B
                follow += 1
                print("[+] Following 1436859892...")
                sleep(2)
                client.user_follow(18428658) #Kim Kardashian
                follow += 1
                print("[+] Following 18428658...")
                sleep(2)
                client.user_follow(7719696) #Ariana Grande
                follow += 1
                print("[+] Following 7719696...")
                sleep(2)
                client.user_follow(451573056) #Nicki Minaj
                follow += 1
                print("[+] Following 451573056...")
                sleep(2)
                client.user_follow(247944034) #Beyonce
                follow += 1
                print("[+] Following 247944034...")
                sleep(2)
                client.user_follow(407964088) #Katy Perry
                follow += 1
                print("[+] Following 407964088...")
                sleep(2)
                client.user_follow(460563723) #Selena Gomez
                follow += 1
                print("[+] Following 460563723...")
                sleep(2)
                client.user_follow(6860189) #Justin Bieber
                follow += 1
                print("[+] Following 6860189...")
                sleep(2)
                client.user_follow(427553890) #Lionel Messi
                follow += 1
                print("[+] Following 427553890...")
                sleep(2)
                client.user_follow(26669533) #Neymar Jr
                follow += 1
                print("[+] Following 26669533...")
                sleep(2)
                client.user_follow(4213518589) #Kylian Mbappe
                follow += 1
                print("[+] Following 4213518589...")
                sleep(2)
                client.user_follow(12331195) #Dua Lipa
                follow += 1
                print("[+] Following 12331195...")
                sleep(2)
                client.user_follow(28527810) #Billie Eilish
                follow += 1
                print("[+] Following 28527810...")
                sleep(2)
                client.user_follow(12281817) #Kylie Jenner
                follow += 1
                print("[+] Following 12281817...")
                sleep(2)
                client.user_follow(208560325) #Khloe Kardashian
                follow += 1
                print("[+] Following 208560325...")
                sleep(2)
                client.user_follow(145821237) #Kourtney Kardashian
                follow += 1
                print("[+] Following 145821237...")
                sleep(2)
                client.user_follow(305701719) #Jennifer Lopez
                follow += 1
                print("[+] Following 305701719...")
                sleep(2)
                client.user_follow(217867189) #Shakira
                follow += 1
                print("[+] Following 217867189...")
                sleep(2)
                client.user_follow(20824486) #NBA
                follow += 1
                print("[+] Following 20824486...")
                sleep(2)
                client.user_follow(25025320) #Instagram
                follow += 1
                print("[+] Following 25025320...")
                sleep(2)
                client.user_follow(787132) #National Geographic
                follow += 1
                print("[+] Following 787132...")
                sleep(2)
                client.user_follow(260375673) #FC Barcelona
                follow += 1
                print("[+] Following 260375673...")
                sleep(2)
                client.user_follow(290023231) #Real Madrid
                follow += 1
                print("[+] Following 290023231...")
                sleep(2)
                client.user_follow(1269788896) #Champions League
                follow += 1
                print("[+] Following 1269788896...")
                sleep(2)
                client.user_follow(29394004) #Chris Brown
                follow += 1
                print("[+] Following 29394004...")
                sleep(2)
                client.user_follow(11830955) #Taylor Swift
                follow += 1
                print("[+] Following 11830955...")
                sleep(2)
                client.user_follow(6380930) #Kendall Jenner
                follow += 1
                print("[+] Following 6380930...")
                sleep(2)
                client.user_follow(2094200507) #Virat Kohli
                follow += 1
                print("[+] Following 2094200507...")
                sleep(2)
                client.user_follow(9777455) #Zendaya
                follow += 1
                print("[+] Following 9777455...")
                sleep(2)
                client.user_unfollow(173560420) #Cristiano Ronaldo
                unfollow += 1
                print("[+] Unfollowing 173560420...")
                sleep(2)
                client.user_unfollow(1436859892) #Cardi B
                unfollow += 1
                print("[+] Unfollowing 1436859892...")
                sleep(2)
                client.user_unfollow(18428658) #Kim Kardashian
                unfollow += 1
                print("[+] Unfollowing 18428658...")
                sleep(2)
                client.user_unfollow(7719696) #Ariana Grande
                unfollow += 1
                print("[+] Unfollowing 7719696...")
                sleep(2)
                client.user_unfollow(451573056) #Nicki Minaj
                unfollow += 1
                print("[+] Unfollowing 451573056...")
                sleep(2)
                client.user_unfollow(247944034) #Beyonce
                unfollow += 1
                print("[+] Unfollowing 247944034...")
                sleep(2)
                client.user_unfollow(407964088) #Katy Perry
                unfollow += 1
                print("[+] Unfollowing 407964088...")
                sleep(2)
                client.user_unfollow(460563723) #Selena Gomez
                unfollow += 1
                print("[+] Unfollowing 460563723...")
                sleep(2)
                client.user_unfollow(6860189) #Justin Bieber
                unfollow += 1
                print("[+] Unfollowing 6860189...")
                sleep(2)
                client.user_unfollow(427553890) #Lionel Messi
                unfollow += 1
                print("[+] Unfollowing 427553890...")
                sleep(2)
                client.user_unfollow(26669533) #Neymar Jr
                unfollow += 1
                print("[+] Unfollowing 26669533...")
                sleep(2)
                client.user_unfollow(4213518589) #Kylian Mbappe
                unfollow += 1
                print("[+] Unfollowing 4213518589...")
                sleep(2)
                client.user_unfollow(12331195) #Dua Lipa
                unfollow += 1
                print("[+] Unfollowing 12331195...")
                sleep(2)
                client.user_unfollow(28527810) #Billie Eilish
                unfollow += 1
                print("[+] Unfollowing 28527810...")
                sleep(2)
                client.user_unfollow(12281817) #Kylie Jenner
                unfollow += 1
                print("[+] Unfollowing 12281817...")
                sleep(2)
                client.user_unfollow(208560325) #Khloe Kardashian
                unfollow += 1
                print("[+] Unfollowing 208560325...")
                sleep(2)
                client.user_unfollow(145821237) #Kourtney Kardashian
                unfollow += 1
                print("[+] Unfollowing 145821237...")
                sleep(2)
                client.user_unfollow(305701719) #Jennifer Lopez
                unfollow += 1
                print("[+] Unfollowing 305701719...")
                sleep(2)
                client.user_unfollow(217867189) #Shakira
                unfollow += 1
                print("[+] Unfollowing 217867189...")
                sleep(2)
                client.user_unfollow(20824486) #NBA
                unfollow += 1
                print("[+] Unfollowing 20824486...")
                sleep(2)
                client.user_unfollow(25025320) #Instagram
                unfollow += 1
                print("[+] Unfollowing 25025320...")
                sleep(2)
                client.user_unfollow(787132) #National Geographic
                unfollow += 1
                print("[+] Unfollowing 787132...")
                sleep(2)
                client.user_unfollow(260375673) #FC Barcelona
                unfollow += 1
                print("[+] Unfollowing 260375673...")
                sleep(2)
                client.user_unfollow(290023231) #Real Madrid
                unfollow += 1
                print("[+] Unfollowing 290023231...")
                sleep(2)
                client.user_unfollow(1269788896) #Champions League
                unfollow += 1
                print("[+] Unfollowing 1269788896...")
                sleep(2)
                client.user_unfollow(29394004) #Chris Brown
                unfollow += 1
                print("[+] Unfollowing 29394004...")
                sleep(2)
                client.user_unfollow(11830955) #Taylor Swift
                unfollow += 1
                print("[+] Unfollowing 11830955...")
                sleep(2)
                client.user_unfollow(6380930) #Kendall Jenner
                unfollow += 1
                print("[+] Unfollowing 6380930...")
                sleep(2)
                client.user_unfollow(2094200507) #Virat Kohli
                unfollow += 1
                print("[+] Unfollowing 2094200507...")
                sleep(2)
                client.user_unfollow(9777455) #Zendaya
                unfollow += 1
                print("[+] Unfollowing 9777455...")
                sleep(2)
            except KeyboardInterrupt:
                pass
            print(f"[✓] Successfully followed: {follow} users")
            sleep(2)
            print(f"[✓] Successfully unfollowed: {unfollow} users")
            sleep(2)
            if follow - unfollow != 0:
                print(f"[✕] Failed to unfollow: {abs(follow - unfollow)} users")
            pers = (follow + unfollow) / 74.0
            print("[+] Percentage of success: "+str(pers))
            sleep(1)
            print(f"[+] Percentage of fail: {float(100 - pers)}%")
            sleep(1)
            if ga in ANS[:9]:
                followers_af = profile.followers
                print(f"[✓] Successfully added: {followers_af - followers_bef} followers.")
                sleep(1)
            print("[1] Return to menu")
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
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
    elif option == 2:
        clear()
        ProgInfo()
    elif option == 3:
        clear()
        name = "log.txt"
        if os.path.exists(os.path.abspath(name)):
            f = open(name,"a")
            f.write("\n"+"-"*40)
            f.write("[+] Date: "+str(date.today())+"\n")
            f.write("[+] Followed: "+str(follow)+" users"+"\n")
            f.write("[+] Unfollowed: "+str(unfollow)+" users"+"\n")
            if follow - unfollow != 0:
                f.write("[✕] Failed to unfollow: "+str(abs(follow - unfollow)+" users"+"\n"))
            pers = (follow + unfollow) / 74.0
            f.write("[+] Percentage of success: "+str(pers)+"%"+"\n")
            f.write("[+] Percentage of fail: "+str(float(100 - pers))+"%"+"\n")
            if ga in ANS[:9]:
                followers_af = profile.followers
                f.write("[✓] Successfully added: "+str(followers_af - followers_bef)+" followers."+"\n")
            f.close()
            print("[✓] Successfully saved log !")
            sleep(2)
            print("[↪] Log file name: "+name)
            print("[↪] Path to log file: "+os.path.abspath(name))
            print("[↪] Log file size: "+str((os.stat(name)).st_size))
            sleep(4)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None:
                if opt == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        else:
            f = open(name,"w")
            f.write("\n"+"-"*40)
            f.write("[+] Date: "+str(date.today())+"\n")
            f.write("[+] Followed: "+str(follow)+" users"+"\n")
            f.write("[+] Unfollowed: "+str(unfollow)+" users"+"\n")
            pers = (follow + unfollow) / 74.0
            f.write("[+] Percentage of success: "+str(pers)+"%"+"\n")
            f.write("[+] Percentage of fail: "+str(float(100 - pers))+"%"+"\n")
            if ga in ANS[:9]:
                followers_af = profile.followers
                f.write("[✓] Successfully added: "+str(followers_af - followers_bef)+" followers."+"\n")
            f.close()
            print("[✓] Successfully saved log !")
            sleep(2)
            print("[↪] Log file name: "+name)
            print("[↪] Path to log file: "+os.path.abspath(name))
            print("[↪] Log file size: "+str((os.stat(name)).st_size))
            sleep(4)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None:
                if opt == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
    elif option == 4:
        clear()
        name = "log.txt"
        if os.path.exists(os.path.abspath(name)):
            f = open(name,"w")
            f.close()
            print("[✓] Successfully cleared log !")
            sleep(1)
            print("[↪] Log file name: "+name)
            print("[↪] Path to log file: "+os.path.abspath(name))
            print("[↪] Log file size: "+str((os.stat(name)).st_size))
            sleep(4)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None:
                if opt == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                sleep(2)
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        else:
            clear()
            print("[!] Log file not found on this device !")
            sleep(2)
            print("[+] Searched log file using name: "+name)
            sleep(2)
            print("[+] Please first create the log file and then use this option 😀")
            sleep(2)
            print("[1] Return to menu")
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
                print("[1] Return to menu")
                print("[2] Exit")
                sleep(2)
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
    elif option == 5:
        clear()
        print(Uninstall())
    else:
        clear()
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
