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
    import platform
    from os import system
    from time import sleep
    import instagrapi
    import os
    import sys
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
    name = 'InstaFollowV1'
    lines = 408
    f = '/IGFollowersIncreaser/InstagramFollowers/V1/mainV1.py'
    ptf = os.path.abspath(f)
    if os.path.exists(ptf):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 14
    forks = stars // 2
    print("[+] Author: "+str(author))
    print("[+] Github: @"+str(author))
    print("[+] License: "+str(license1))
    print("[+] Natural language: "+str(lang))
    print("[+] Programming language(s) used: "+str(language))
    print("[+] Number of lines: "+str(lines))
    print("[+] Program's name: "+str(name))
    print("[+] File size: "+str(fsize)+" bytes")
    print("[+] Github repo stars: "+str(stars))
    print("[+] Github repo forks: "+str(forks))

def banner(): 
    return """
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗░░███╗░░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║░████║░░
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝██╔██║░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░╚═╝██║░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
"""

def nums():
    print("[1] Increase followers")
    print("[2] Show program info and exit")
    print("[3] Uninstall script")
    print("[4] Exit")

def main():
    banner()
    print("\n")
    print("[+] Program for increasing followers on Instagram")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    nums()
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 4 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        nums()
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
        sleep(1)
        print("[+] The data will not be stored or saved")
        sleep(2)
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
                print("[+] See you next time 👋")
                sleep(1)
                exit(0)
        username=username.lower()
        username=username.strip()
        sleep(1)
        password=input("[::] Please enter your password: ")
        while password == None:
            print("[!] Invalid password !")
            sleep(1)
            password=input("[::] Please enter again your password: ")
        password=password.strip()
        sleep(1)
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
                sleep(1)
                print("[+] Exiting...")
                quit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(1)
            print("[+] Exiting...")
            quit(0)
        sleep(2)
        print("[+] To end the process enter Ctrl + C")
        sleep(2)
        print("[!] NOTE: Use this program every 2 days in order for your account not to get blocked")
        while True:
            try:
                clnt.user_follow(173560420) #Cristiano Ronaldo
                print("[+] Following 173560420...")
                sleep(2)
                clnt.user_follow(1436859892) #Cardi B
                print("[+] Following 1436859892...")
                sleep(2)
                clnt.user_follow(18428658) #Kim Kardashian
                print("[+] Following 18428658...")
                sleep(2)
                clnt.user_follow(7719696) #Ariana Grande
                print("[+] Following 7719696...")
                sleep(2)
                clnt.user_follow(451573056) #Nicki Minaj
                print("[+] Following 451573056...")
                sleep(2)
                clnt.user_follow(247944034) #Beyonce
                print("[+] Following 247944034...")
                sleep(2)
                clnt.user_follow(407964088) #Katy Perry
                print("[+] Following 407964088...")
                sleep(2)
                clnt.user_follow(460563723) #Selena Gomez
                print("[+] Following 460563723...")
                sleep(2)
                clnt.user_follow(6860189) #Justin Bieber
                print("[+] Following 6860189...")
                sleep(2)
                clnt.user_follow(427553890) #Lionel Messi
                print("[+] Following 427553890...")
                sleep(2)
                clnt.user_follow(26669533) #Neymar Jr
                print("[+] Following 26669533...")
                sleep(2)
                clnt.user_follow(4213518589) #Kylian Mbappe
                print("[+] Following 4213518589...")
                sleep(2)
                clnt.user_follow(12331195) #Dua Lipa
                print("[+] Following 12331195...")
                sleep(2)
                clnt.user_follow(28527810) #Billie Eilish
                print("[+] Following 28527810...")
                sleep(2)
                clnt.user_follow(12281817) #Kylie Jenner
                print("[+] Following 12281817...")
                sleep(2)
                clnt.user_follow(208560325) #Khloe Kardashian
                print("[+] Following 208560325...")
                sleep(2)
                clnt.user_follow(145821237) #Kourtney Kardashian
                print("[+] Following 145821237...")
                sleep(2)
                clnt.user_follow(305701719) #Jennifer Lopez
                print("[+] Following 305701719...")
                sleep(2)
                clnt.user_follow(217867189) #Shakira
                print("[+] Following 217867189...")
                sleep(2)
                clnt.user_follow(20824486) #NBA
                print("[+] Following 20824486...")
                sleep(2)
                clnt.user_follow(25025320) #Instagram
                print("[+] Following 25025320...")
                sleep(2)
                clnt.user_follow(787132) #National Geographic
                print("[+] Following 787132...")
                sleep(2)
                clnt.user_follow(260375673) #FC Barcelona
                print("[+] Following 260375673...")
                sleep(2)
                clnt.user_follow(290023231) #Real Madrid
                print("[+] Following 290023231...")
                sleep(2)
                clnt.user_follow(1269788896) #Champions League
                print("[+] Following 1269788896...")
                sleep(2)
                clnt.user_follow(29394004) #Chris Brown
                print("[+] Following 29394004...")
                sleep(2)
                clnt.user_follow(11830955) #Taylor Swift
                print("[+] Following 11830955...")
                sleep(2)
                clnt.user_follow(6380930) #Kendall Jenner
                print("[+] Following 6380930...")
                sleep(2)
                clnt.user_follow(2094200507) #Virat Kohli
                print("[+] Following 2094200507...")
                sleep(2)
                clnt.user_follow(9777455) #Zendaya
                print("[+] Following 9777455...")
                sleep(2)
                clnt.user_unfollow(173560420) #Cristiano Ronaldo
                print("[+] Unfollowing 173560420...")
                sleep(2)
                clnt.user_unfollow(1436859892) #Cardi B
                print("[+] Unfollowing 1436859892...")
                sleep(2)
                clnt.user_unfollow(18428658) #Kim Kardashian
                print("[+] Unfollowing 18428658...")
                sleep(2)
                clnt.user_unfollow(7719696) #Ariana Grande
                print("[+] Unfollowing 7719696...")
                sleep(2)
                clnt.user_unfollow(451573056) #Nicki Minaj
                print("[+] Unfollowing 451573056...")
                sleep(2)
                clnt.user_unfollow(247944034) #Beyonce
                print("[+] Unfollowing 247944034...")
                sleep(2)
                clnt.user_unfollow(407964088) #Katy Perry
                print("[+] Unfollowing 407964088...")
                sleep(2)
                clnt.user_unfollow(460563723) #Selena Gomez
                print("[+] Unfollowing 460563723...")
                sleep(2)
                clnt.user_unfollow(6860189) #Justin Bieber
                print("[+] Unfollowing 6860189...")
                sleep(2)
                clnt.user_unfollow(427553890) #Lionel Messi
                print("[+] Unfollowing 427553890...")
                sleep(2)
                clnt.user_unfollow(26669533) #Neymar Jr
                print("[+] Unfollowing 26669533...")
                sleep(2)
                clnt.user_unfollow(4213518589) #Kylian Mbappe
                print("[+] Unfollowing 4213518589...")
                sleep(2)
                clnt.user_unfollow(12331195) #Dua Lipa
                print("[+] Unfollowing 12331195...")
                sleep(2)
                clnt.user_unfollow(28527810) #Billie Eilish
                print("[+] Unfollowing 28527810...")
                sleep(2)
                clnt.user_unfollow(12281817) #Kylie Jenner
                print("[+] Unfollowing 12281817...")
                sleep(2)
                clnt.user_unfollow(208560325) #Khloe Kardashian
                print("[+] Unfollowing 208560325...")
                sleep(2)
                clnt.user_unfollow(145821237) #Kourtney Kardashian
                print("[+] Unfollowing 145821237...")
                sleep(2)
                clnt.user_unfollow(305701719) #Jennifer Lopez
                print("[+] Unfollowing 305701719...")
                sleep(2)
                clnt.user_unfollow(217867189) #Shakira
                print("[+] Unfollowing 217867189...")
                sleep(2)
                clnt.user_unfollow(20824486) #NBA
                print("[+] Unfollowing 20824486...")
                sleep(2)
                clnt.user_unfollow(25025320) #Instagram
                print("[+] Unfollowing 25025320...")
                sleep(2)
                clnt.user_unfollow(787132) #National Geographic
                print("[+] Unfollowing 787132...")
                sleep(2)
                clnt.user_unfollow(260375673) #FC Barcelona
                print("[+] Unfollowing 260375673...")
                sleep(2)
                clnt.user_unfollow(290023231) #Real Madrid
                print("[+] Unfollowing 290023231...")
                sleep(2)
                clnt.user_unfollow(1269788896) #Champions League
                print("[+] Unfollowing 1269788896...")
                sleep(2)
                clnt.user_unfollow(29394004) #Chris Brown
                print("[+] Unfollowing 29394004...")
                sleep(2)
                clnt.user_unfollow(11830955) #Taylor Swift
                print("[+] Unfollowing 11830955...")
                sleep(2)
                clnt.user_unfollow(6380930) #Kendall Jenner
                print("[+] Unfollowing 6380930...")
                sleep(2)
                clnt.user_unfollow(2094200507) #Virat Kohli
                print("[+] Unfollowing 2094200507...")
                sleep(2)
                clnt.user_unfollow(9777455) #Zendaya
                print("[+] Unfollowing 9777455...")
                sleep(2)
            except KeyboardInterrupt as key:
                print("[!] Program Interrupted !")
                sleep(1)
                print("[+] Exiting...")
                quit(0)
    elif option == 2:
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
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
        print("[+] Files uninstalled successfully !")
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
