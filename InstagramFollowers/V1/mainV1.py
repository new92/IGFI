"""
Author: @new92
InstaFollow: Program for increasing followers on Instagram
User's data (such as: username, password) will not be stored or saved ! 
Will be used only to increase the followers of the given account
"""

#Imports
try:
    import time
    import platform
    from os import system
    import instagrapi
    import socket
    import requests
    import os
    import logging
    import instabot
    import instapy
    import webbrowser
    import sys
    import instaloader
    import getpass
    import http
    import art
    from art import tprint
    from getpass import getpass
    from instagrapi import *
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
tprint("INSTAFOLLOW    V1",font="tarty1")

#Main program
print("\n")
print("[+] Program for increasing followers on Instagram")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[1] Increase Followers")
print("[2] Exit")
print("\n")
option=int(input("[::] Choose an option: "))

while option <= 0 or option > 2 or option == None:
    print("[!] Invalid option !")
    time.sleep(1)
    option=int(input("[::] Please enter again the option: "))
if option == 1:
    time.sleep(1)
    print("[+] The data will not be stored or saved")
    time.sleep(2)
    username=input("[::] Please enter your username: ")
    while username == None or len(username) > 30:
        print("[!] Invalid Username !")
        time.sleep(1)
        username=input("[::] Please enter again your username: ")
    username=username.lower()
    username=username.strip()
    time.sleep(1)
    password=input("[::] Please enter your password: ")
    while password == None:
        print("[!] Invalid Password !")
        time.sleep(1)
        password=input("[::] Please enter again your password: ")
    password=password.strip()
    time.sleep(1)
    clnt=instagrapi.Client()
    try:
        login = clnt.login(username,password)
        if login == True:
            print("[!] Login Successful !")
            time.sleep(2)
            print("[+] Please wait while the program is increasing your followers...")
        else:
            print("[!] Login Unsuccessful !")
            time.sleep(2)
            print("[+] Please check the username and/or the password !")
            time.sleep(1)
            print("[+] Exiting...")
            exit(0)
    except Exception as e:
        print("[!] Unexpected Error !")
        time.sleep(1)
        print(e)
        time.sleep(1)
        print("[+] Exiting...")
        exit(0)
    time.sleep(2)
    print("[+] To end the process enter Ctrl + C")
    time.sleep(2)
    c = 1
    print("[!] NOTE: Use this program every 2 days in order for your account not to get blocked")
    while c > 0:
        try:
            clnt.user_follow(173560420) #Cristiano Ronaldo
            print("[+] Following 173560420...")
            time.sleep(2)
            clnt.user_follow(1436859892) #Cardi B
            print("[+] Following 1436859892...")
            time.sleep(2)
            clnt.user_follow(18428658) #Kim Kardashian
            print("[+] Following 18428658...")
            time.sleep(2)
            clnt.user_follow(7719696) #Ariana Grande
            print("[+] Following 7719696...")
            time.sleep(2)
            clnt.user_follow(451573056) #Nicki Minaj
            print("[+] Following 451573056...")
            time.sleep(2)
            clnt.user_follow(247944034) #Beyonce
            print("[+] Following 247944034...")
            time.sleep(2)
            clnt.user_follow(407964088) #Katy Perry
            print("[+] Following 407964088...")
            time.sleep(2)
            clnt.user_follow(460563723) #Selena Gomez
            print("[+] Following 460563723...")
            time.sleep(2)
            clnt.user_follow(6860189) #Justin Bieber
            print("[+] Following 6860189...")
            time.sleep(2)
            clnt.user_follow(427553890) #Lionel Messi
            print("[+] Following 427553890...")
            time.sleep(2)
            clnt.user_follow(26669533) #Neymar Jr
            print("[+] Following 26669533...")
            time.sleep(2)
            clnt.user_follow(4213518589) #Kylian Mbappe
            print("[+] Following 4213518589...")
            time.sleep(2)
            clnt.user_follow(12331195) #Dua Lipa
            print("[+] Following 12331195...")
            time.sleep(2)
            clnt.user_follow(28527810) #Billie Eilish
            print("[+] Following 28527810...")
            time.sleep(2)
            clnt.user_follow(12281817) #Kylie Jenner
            print("[+] Following 12281817...")
            time.sleep(2)
            clnt.user_follow(208560325) #Khloe Kardashian
            print("[+] Following 208560325...")
            time.sleep(2)
            clnt.user_follow(145821237) #Kourtney Kardashian
            print("[+] Following 145821237...")
            time.sleep(2)
            clnt.user_follow(305701719) #Jennifer Lopez
            print("[+] Following 305701719...")
            time.sleep(2)
            clnt.user_follow(217867189) #Shakira
            print("[+] Following 217867189...")
            time.sleep(2)
            clnt.user_follow(20824486) #NBA
            print("[+] Following 20824486...")
            time.sleep(2)
            clnt.user_follow(25025320) #Instagram
            print("[+] Following 25025320...")
            time.sleep(2)
            clnt.user_follow(787132) #National Geographic
            print("[+] Following 787132...")
            time.sleep(2)
            clnt.user_follow(260375673) #FC Barcelona
            print("[+] Following 260375673...")
            time.sleep(2)
            clnt.user_follow(290023231) #Real Madrid
            print("[+] Following 290023231...")
            time.sleep(2)
            clnt.user_follow(1269788896) #Champions League
            print("[+] Following 1269788896...")
            time.sleep(2)
            clnt.user_follow(29394004) #Chris Brown
            print("[+] Following 29394004...")
            time.sleep(2)
            clnt.user_follow(11830955) #Taylor Swift
            print("[+] Following 11830955...")
            time.sleep(2)
            clnt.user_follow(6380930) #Kendall Jenner
            print("[+] Following 6380930...")
            time.sleep(2)
            clnt.user_follow(2094200507) #Virat Kohli
            print("[+] Following 2094200507...")
            time.sleep(2)
            clnt.user_follow(9777455) #Zendaya
            print("[+] Following 9777455...")
            time.sleep(2)
            clnt.user_unfollow(173560420) #Cristiano Ronaldo
            print("[+] Unfollowing 173560420...")
            time.sleep(2)
            clnt.user_unfollow(1436859892) #Cardi B
            print("[+] Unfollowing 1436859892...")
            time.sleep(2)
            clnt.user_unfollow(18428658) #Kim Kardashian
            print("[+] Unfollowing 18428658...")
            time.sleep(2)
            clnt.user_unfollow(7719696) #Ariana Grande
            print("[+] Unfollowing 7719696...")
            time.sleep(2)
            clnt.user_unfollow(451573056) #Nicki Minaj
            print("[+] Unfollowing 451573056...")
            time.sleep(2)
            clnt.user_unfollow(247944034) #Beyonce
            print("[+] Unfollowing 247944034...")
            time.sleep(2)
            clnt.user_unfollow(407964088) #Katy Perry
            print("[+] Unfollowing 407964088...")
            time.sleep(2)
            clnt.user_unfollow(460563723) #Selena Gomez
            print("[+] Unfollowing 460563723...")
            time.sleep(2)
            clnt.user_unfollow(6860189) #Justin Bieber
            print("[+] Unfollowing 6860189...")
            time.sleep(2)
            clnt.user_unfollow(427553890) #Lionel Messi
            print("[+] Unfollowing 427553890...")
            time.sleep(2)
            clnt.user_unfollow(26669533) #Neymar Jr
            print("[+] Unfollowing 26669533...")
            time.sleep(2)
            clnt.user_unfollow(4213518589) #Kylian Mbappe
            print("[+] Unfollowing 4213518589...")
            time.sleep(2)
            clnt.user_unfollow(12331195) #Dua Lipa
            print("[+] Unfollowing 12331195...")
            time.sleep(2)
            clnt.user_unfollow(28527810) #Billie Eilish
            print("[+] Unfollowing 28527810...")
            time.sleep(2)
            clnt.user_unfollow(12281817) #Kylie Jenner
            print("[+] Unfollowing 12281817...")
            time.sleep(2)
            clnt.user_unfollow(208560325) #Khloe Kardashian
            print("[+] Unfollowing 208560325...")
            time.sleep(2)
            clnt.user_unfollow(145821237) #Kourtney Kardashian
            print("[+] Unfollowing 145821237...")
            time.sleep(2)
            clnt.user_unfollow(305701719) #Jennifer Lopez
            print("[+] Unfollowing 305701719...")
            time.sleep(2)
            clnt.user_unfollow(217867189) #Shakira
            print("[+] Unfollowing 217867189...")
            time.sleep(2)
            clnt.user_unfollow(20824486) #NBA
            print("[+] Unfollowing 20824486...")
            time.sleep(2)
            clnt.user_unfollow(25025320) #Instagram
            print("[+] Unfollowing 25025320...")
            time.sleep(2)
            clnt.user_unfollow(787132) #National Geographic
            print("[+] Unfollowing 787132...")
            time.sleep(2)
            clnt.user_unfollow(260375673) #FC Barcelona
            print("[+] Unfollowing 260375673...")
            time.sleep(2)
            clnt.user_unfollow(290023231) #Real Madrid
            print("[+] Unfollowing 290023231...")
            time.sleep(2)
            clnt.user_unfollow(1269788896) #Champions League
            print("[+] Unfollowing 1269788896...")
            time.sleep(2)
            clnt.user_unfollow(29394004) #Chris Brown
            print("[+] Unfollowing 29394004...")
            time.sleep(2)
            clnt.user_unfollow(11830955) #Taylor Swift
            print("[+] Unfollowing 11830955...")
            time.sleep(2)
            clnt.user_unfollow(6380930) #Kendall Jenner
            print("[+] Unfollowing 6380930...")
            time.sleep(2)
            clnt.user_unfollow(2094200507) #Virat Kohli
            print("[+] Unfollowing 2094200507...")
            time.sleep(2)
            clnt.user_unfollow(9777455) #Zendaya
            print("[+] Unfollowing 9777455...")
            time.sleep(2)
        except KeyboardInterrupt as key:
            print("[!] Program Interrupted !")
            time.sleep(1)
            print("[+] Exiting...")
            exit(0)
else:
    print("[+] Exiting...")
    exit(0)
