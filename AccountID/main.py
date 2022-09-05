"""
Author: @new92
InstaID: Program for getting, displaying and saving the ID of an Instagram account
"""
#Imports
try:
    import os
    import platform
    from os import system
    import sys
    import instagrapi
    import instabot
    import instaloader
    import instapy
    import instagram_private_api
    import instagram_web_api
    import webbrowser
    import time
    from art import tprint
    from selenium import webdriver
except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    time.sleep(2)
    print("[+] Ignoring Warning...")
    time.sleep(1)
    if platform.system() == "Windows":
        system("pip3 install -r requirements.txt")
    else:
        system("sudo pip3 install -r requirements.txt")

#Logo
tprint("INSTAID", font="tarty1")

#Main Program
print("\n")
print("[+] InstaID: Program for getting and displaying the ID of an instagram account !")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Get account ID")
print("[2] Exit")
print("\n")
option=int(input("[::] Choose an option: "))

while option < 1 or option > 2 or option == None:
    print("[!] Invalid option !")
    time.sleep(1)
    option=int(input("[::] Please enter again: "))

if option == 1:
    username=str(input("[::] Please enter the username: "))
    while username == None or len(username) > 30:
        print("[!] Invalid Username !")
        time.sleep(2)
        username=str(input("[::] Please enter again the username: "))
    username=username.lower()
    username=username.strip()
    loader=instaloader.Instaloader()
    id=loader.check_profile_id(username)
    time.sleep(3)
    print("[+] The id has been saved in a folder in the current folder with the name: "+str(username))
    time.sleep(2)
    exit(0)

else:
    print("[+] Exiting...")
    exit(0)
