"""
Author: @new92
InstaFollowV2: Is a program similar to Version 1 (V1) but I found a different way to make the same program with less
lines of code.
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
tprint("INSTAFOLLOW    V2",font="tarty1")

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

while option < 1 or option > 2 or option == None:
    print("[!] Invalid option !")
    time.sleep(1)
    option=int(input("[::] Please enter again: "))
if option == 1:
    print("[+] The data will not be stored or saved")
    time.sleep(2)
    username=str(input("[::] Please enter your username: "))
    while username == None or len(username) > 30:
        print("[!] Invalid Username !")
        time.sleep(1)
        username=str(input("[::] Please enter again your username: "))
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
            time.sleep(2)
            print("[+] Exiting...")
            exit(0)
    except Exception as ex:
        print("[!] Unexpected Error !")
        time.sleep(1)
        print(ex)
        time.sleep(2)
        print("[+] Exiting...")
        exit(0)
    time.sleep(2)
    print("[+] To end the process enter Ctrl + C")
    time.sleep(2)
    c = 1
    FOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455']
    UNFOLLOW=['173560420','1436859892','18428658','7719696','451573056','247944034','407964088','460563723','6860189','427553890','26669533','4213518589','12331195','28527810','12281817','208560325','145821237','305701719','217867189','20824486','25025320','787132','260375673','290023231','1269788896','29394004','11830955','6380930','2094200507','9777455']
    print("[!] NOTE: Use this program every 2 days in order for your account not to get blocked")
    time.sleep(5)
    while c > 0:
        for i in range(len(FOLLOW)):
            try:
                clnt.user_follow(FOLLOW[i])
            except Exception as ex:
                print("[!] Error !")
                time.sleep(1)
                print(ex)
                time.sleep(2)
                print("[+] Exiting...")
                exit(0)
            print("[+] Following "+str(FOLLOW[i])+"...")
            time.sleep(1)
        for e in range(len(UNFOLLOW)):
            try:
                clnt.user_unfollow(UNFOLLOW[e])
            except Exception as ex:
                print("[!] Error !")
                time.sleep(1)
                print(ex)
                time.sleep(2)
                print("[+] Exiting...")
                exit(0)
            print("[+] Unfollowing "+str(UNFOLLOW[e])+"...")
            time.sleep(1)
