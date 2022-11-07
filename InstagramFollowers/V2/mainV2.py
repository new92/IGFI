"""
Author: new92
Github: https://www.github.com/new92
InstaFollowV2: Is a program similar to Version 1 (V1) but I found a different way to build the same program with less
lines of code.
User's data (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the user's account
"""

#Imports
try:
    import sys
    import platform
    from os import system
    from time import sleep
    import instagrapi
    import webbrowser
    import os
    import requests
    import instabot
    import instapy
    import instaloader
    import instagram_private_api
    from getpass import getpass
    from instagrapi import *
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring Warning...")
    sleep(1)
    if sys.platform.startswith('linux') == True:
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip3 install -r requirements.txt")
        pass


print("""
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗    ██╗░░░██╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║    ██║░░░██║╚════██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝    ╚██╗░██╔╝░░███╔═╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░    ░╚████╔╝░██╔══╝░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░    ░░╚██╔╝░░███████╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░    ░░░╚═╝░░░╚══════╝
""")
print("\n")
print("[+] Program for increasing followers on Instagram")
print("\n")
print("[+] Github: https://www.github.com/new92")
print("\n")
print("[1] Increase Followers")
print("[2] Exit")
print("\n")
option=int(input("[::] Please enter the number of the option (from above): "))
while option < 1 or option > 2 or option == None:
    print("[!] Invalid number !")
    sleep(1)
    option=int(input("[::] Please enter again: "))
if option == 1:
    print("[+] The data will not be stored or saved")
    sleep(2)
    while username == None or len(username) > 30:
        print("[!] Invalid Username !")
        sleep(1)
        username=str(input("[::] Please enter again your username: "))
    username=str(input("[::] Please enter your username: "))
    resp = requests.get(f"https://www.instagram.com/{username}/")
    while resp.status_code == 404 or resp.status_code == 400:
        print("[!] User not found !")
        sleep(1)
        print("[1] Try with another username")
        print("[2] Exit")
        opt=int(input(">>> "))
        while opt < 1 or opt > 2 or opt == None:
            print("[!] Invalid number !")
            sleep(1)
            opt=int(input(">>> "))
        if opt == 1:
            username=str(input("[::] Please enter the username: "))
            while username == None:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter the username: "))
            continue
        else:
            print("[+] Exiting...")
            quit(0)
    username=username.lower()
    username=username.strip()
    sleep(1)
    password=input("[::] Please enter your password: ")
    while password == None:
        print("[!] Invalid Password !")
        sleep(1)
        password=input("[::] Please enter again your password: ")
    password=password.strip()
    sleep(1)
    clnt=instagrapi.Client()
    try:
        login = clnt.login(username,password)
        if login == True:
            print("[!] Login Successful !")
            sleep(1)
            print("[+] Please wait while the program is increasing your followers...")
            sleep(2)
        else:
            print("[!] Login Unsuccessful !")
            sleep(1)
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
    c = 1
    FOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455']
    UNFOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455']
    print("[!] NOTE: Use this program every 2 days in order for your account not to get blocked")
    sleep(5)
    while c > 0:
        for i in range(len(FOLLOW)):
            try:
                clnt.user_follow(FOLLOW[i])
            except Exception as key:
                print("[!] Error !")
                sleep(1)
                print(key)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
            print(f"[+] Following {FOLLOW[i]}...")
            sleep(1)
        for j in range(len(UNFOLLOW)):
            try:
                clnt.user_unfollow(UNFOLLOW[j])
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
            print(f"[+] Unfollowing {UNFOLLOW[e]}...")
            sleep(1)
