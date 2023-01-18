"""
Author: new92
Github: @new92
InstaFollowV2: Script for increasing the followers of an Instagram account

*********IMPORTANT*********

User's data (such as: username, password) will not be stored or saved ! 
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


banner = """
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║╚════██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝░░███╔═╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░██╔══╝░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
"""
print(banner)
print("\n")
print("[+] Script for increasing the followers of an account on Instagram (works for both public and private accounts)")
print("\n")
print("[+] Author: new92")
print("[+] Github: @new92")
print("\n")
print("[1] Increase followers")
print("[2] Exit")
print("\n")
option=int(input("[::] Please enter a number of the option (from above): "))
while option < 1 or option > 2 or option == None:
    print("[!] Invalid number !")
    sleep(1)
    option=int(input("[::] Please enter again the number: "))
if option == 1:
    print("[+] The login data will not be stored or saved")
    sleep(2)
    print("|"+"-"*20+"login".upper()+"-"*20+"|")
    username=str(input("[::] Please enter your username: "))
    while username == None or len(username) > 30:
        print("[!] Invalid username !")
        sleep(1)
        username=str(input("[::] Please enter again your username: "))
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
            sleep(2)
            print("[+] Exiting...")
            quit(0)
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
