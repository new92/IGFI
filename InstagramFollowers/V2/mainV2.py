# -*- coding: utf-8 -*-
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
    if sys.version_info[0] < 3:
        print("[!] Error ! This script requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        print("[+] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from os import system
    from time import sleep
    import os
    import instagrapi
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
                print("[=] Error message -> "+str(ex))
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
    license1 = 'MIT'
    lang = 'es-US'
    language = 'Python'
    name = 'InstaFollowV2'
    api = None
    lines = 735
    f = '/IGFollowersIncreaser/InstagramFollowers/V2/mainV2.py'
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 18
    forks = 10
    print("[+] Author: "+author)
    print("[+] Github: @"+author)
    print("[+] License: "+license1)
    print("[+] Natural language: "+lang)
    print("[+] Programming language(s) used: "+str(language))
    print("[+] Number of lines: "+str(lines))
    print("[+] Script's name: "+str(name))
    print("[+] API(s) used: "+str(api))
    print("[+] File size: "+str(fsize)+" bytes")
    print("[+] Github repo stars: "+str(stars))
    print("[+] Github repo forks: "+str(forks))

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


def banner() -> str:
  return """
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║╚════██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝░░███╔═╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░██╔══╝░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
"""

def checkUser(username:str) -> bool:
    return username == None or len(username) > 30 or type(username) != str

def nums():
    print("[1] Increase followers")
    print("[2] Show script's info and exit")
    print("[3] Keep log")
    print("[4] Clear log")
    print("[5] Uninstall script")
    print("[6] Exit")

def clear():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

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
        if os.path.exists("cons.txt"):
            con=str(input("[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? [yes/no] "))
            if con in ANS[:9]:
                f = open("cons.txt","a")
                f.write("[=] Date: "+str(date.today())+"\n")
                f.write("[=] User: Yes I consent that the author of this script (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
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
                    clear()
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] Until we meet again 👋")
                    sleep(1)
                    quit(0)
        else:
            f = open("cons.txt","w")
            f.write("[=] Date: "+str(date.today())+"\n")
            f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
            f.write("-"*40)
            f.close()
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
                print("[+] Acceptable length: less than or equal to 30")
            sleep(1)
            username=str(input("[>] Please enter again your username: "))
        while requests.get(f"https://www.instagram.com/{username}/").status_code == 404 or requests.get(f"https://www.instagram.com/{username}/").status_code == 400:
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Uninstall and Exit")
            print("[4] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 4 or opt == None:
                if opt == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2/3/4]")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Uninstall and Exit")
                print("[4] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                username=str(input("[>] Please enter the username: "))
                while checkUser(username):
                    if username == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid length  !")
                        sleep(1)
                        print("[+] The length of the username must be less than or equal to 30 characters.")
                    sleep(1)
                    username=str(input("[>] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            elif opt == 3:
                clear()
                print(Uninstall())
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] Hope you enjoyed it ! ☺️")
                sleep(2)
                print("[+] Until next time 👋")
                sleep(1)
                quit(0)
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        con=str(input(f"[?] Script will increase the followers for the user: {username} is that correct ? [yes/no] "))
        while con not in ANS or con == None or type(con) != str:
            if con == None:
                print("[!] This field can't be blank !")
            elif type(con) != str:
                print("[!] You must enter a string !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"[?] Script will increase the followers for the user: {username} is it correct ? [yes/no] "))
        if con in ANS[9:]:
            username=str(input("[>] Please enter an other username: "))
            while checkUser(username):
                if username == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid length !")
                    sleep(1)
                    print("[+] Acceptable length: less than or equal to 30")
                sleep(1)
                username=str(input("[>] Please enter again your username: "))
            while requests.get(f"https://www.instagram.com/{username}/").status_code == 404 or requests.get(f"https://www.instagram.com/{username}/").status_code == 400:
                print("[!] User not found !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Uninstall and Exit")
                print("[4] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 4 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2/3/4]")
                    sleep(1)
                    print("[1] Try with another username")
                    print("[2] Return to menu")
                    print("[3] Uninstall and Exit")
                    print("[4] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    clear()
                    username=str(input("[>] Please enter the username: "))
                    while checkUser(username):
                        if username == None:
                            print("[!] This field can't be blank !")
                        else:
                            print("[!] Invalid length  !")
                            sleep(1)
                            print("[+] The length of the username must be less than or equal to 30 characters.")
                        sleep(1)
                        username=str(input("[>] Please enter again the username: "))
                elif opt == 2:
                    clear()
                    main()
                elif opt == 3:
                    clear()
                    print(Uninstall())
                    print("[+] Thank you for using my script 😁")
                    sleep(2)
                    print("[+] Hope you enjoyed it ! ☺️")
                    sleep(2)
                    print("[+] Until next time 👋")
                    sleep(1)
                    quit(0)
                else:
                    clear()
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        ga=str(input("[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? [yes/no] "))
        while ga not in ANS or ga == None or type(ga) != str:
            if ga == None:
                print("[!] This field can't be blank !")
            elif type(ga) != str:
                print("[!] Your input must be a string !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Valid answers: [yes/no]")
            sleep(1)
            ga=str(input("[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? [yes/no] "))
        if ga in ANS[:9]:
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username)
            followers_bef = profile.followers
        username=username.lower()
        username=username.strip()
        sleep(1)
        password=str(input("[>] Please enter your password: "))
        while password == None or type(password) != str:
            if password == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid password !")
                sleep(1)
                print("[+] The password must be a string")
            sleep(1)
            password=str(input("[>] Please enter again your password: "))
        password=password.strip()
        sleep(1)
        print("|"+"-"*45+"|")
        client=instagrapi.Client()
        try:
            login = client.login(username,password)
            if login:
                print("[✓] Login successful !")
                sleep(2)
                print("[+] Please wait while the program is increasing your followers...")
            else:
                print("[✕] Login unsuccessful !")
                sleep(2)
                print("[+] Please check the username and/or the password !")
                sleep(2)
                print("\n")
                print("[1] Return to menu")
                print("[2] Uninstall and Exit")
                print("[3] Exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 3 or num == None:
                    if num == None:
                        print("[!] This field can't be empty !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2/3]")
                    sleep(1)
                    num=int(input("[>] Please enter again a number (from the above ones):"))
                if num == 1:
                    clear()
                    main()
                elif num == 2:
                    clear()
                    print(Uninstall())
                    print("[+] Thank you for using my script 😁")
                    sleep(2)
                    print("[+] Until we meet again 👋")
                    sleep(1)
                    quit(0)
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        except Exception as e:
            print("[!] Error !")
            sleep(1)
            print(f"[*] Error message ==> {e}")
            sleep(2)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[>] Please enter a number (from the above ones): "))
            while num < 1 or num > 2 or num == None or type(num) != int:
                if num == None:
                    print("[!] This field can't be empty !")
                elif type(num) != int:
                    print("[!] Number must be an integer !")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter again a number (from the above ones): "))
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
        sleep(1)
        FOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455','204633036','176618189','1418652011','3439002676','212742998','528817151','13460080']
        NAMES = ['Cristiano Ronaldo','Cardi B','Kim Kardashian','Ariana Grande','Nicki Minaj','Beyonce','Katy Perry','Selena Gomez','Justin Bieber','Lionel Messi','Neymar Jr','Kylian Mbappe','Dua Lipa','Billie Eilish','Kylie Jenner','Khloe Kardashian','Kourtney Kardashian','Jennifer Lopez','Shakira','NBA','Instagram','National Geographic','FC Barcelona','Real Madrid','Champions League','Chris Brown','Taylor Swift','Kendall Jenner','Virat Kohli','Zendaya','Marvel','Tom Holland','Emma Watson','Millie Bobby Brown','Shawn Mendes','NASA','Nike']
        print("[*] NOTE: Use this program every 2 days in order for your account not to get blocked")
        sleep(3)
        follow = 0
        unfollow = 0
        while True:
            try:
                for i in range(len(FOLLOW)-1):
                    client.user_follow(FOLLOW[i])
                    follow += 1
                    print(f"[+] Following {NAMES[i]}...")
                    sleep(2)
                    print(f"[+] Next user to follow: {NAMES[i+1]}")
                    sleep(3)
                for i in range(len(FOLLOW)-1):
                    client.user_unfollow(FOLLOW[i])
                    unfollow += 1
                    print(f"[+] Unfollowing {NAMES[i]}...")
                    sleep(3)
                    print(f"[+] Next user to unfollow: {NAMES[i+1]}")
                    sleep(1)
            except Exception:
                print(f"[✓] Successfully followed: {follow} users")
                sleep(2)
                print(f"[✓] Successfully unfollowed: {unfollow} users")
                sleep(2)
                if follow - unfollow != 0:
                    print(f"[✕] Failed to unfollow: {abs(follow - unfollow)} users")
                pers = (follow + unfollow) / float(len(FOLLOW)*2)
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
            pers = (follow + unfollow) / float(len(FOLLOW)*2)
            f.write("[+] Percentage of success: "+str(pers)+"%"+"\n")
            f.write("[+] Percentage of fail: "+str(float(100 - pers))+"%"+"\n")
            if ga in ANS[:9]:
                followers_af = profile.followers
                f.write("[✓] Successfully added: "+str(followers_af - followers_bef)+" followers.")
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
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print("[!] Number must be an integer !")
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
        else:
            f = open(name,"w")
            f.write("\n"+"-"*40)
            f.write("[+] Date: "+str(date.today())+"\n")
            f.write("[+] Followed: "+str(follow)+" users"+"\n")
            f.write("[+] Unfollowed: "+str(unfollow)+" users"+"\n")
            pers = (follow + unfollow) / float(len(FOLLOW)*2)
            f.write("[+] Percentage of success: "+str(pers)+"%"+"\n")
            f.write("[+] Percentage of fail: "+str(float(100 - pers))+"%"+"\n")
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
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print("[!] You must enter an integer !")
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
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print("[!] You must enter an integer !")
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
        else:
            clear()
            print("[!] Log file not found on this device !")
            sleep(2)
            print("[+] Searched log file using name: "+name)
            sleep(2)
            print("[*] Please first create the log file and then use this option 😀")
            sleep(2)
            print("""[+] Instructions: 
            1) Return to menu and enter the option number 3
            2) Wait for the script to end and execute it again
            3) From the menu enter the number 4.
            """)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print("[!] You must enter an integer !")
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
