print("password generator. y or n for all prompts")
import os
import random
menu = input("1.Input\n2.View Passwords\n3.Make New")
if menu == "1":
    inputs = input("input?: ")
    if inputs == "y":
        websiteask = input("website?: ")
        if websiteask == "n":
            print("ok")
            password = input("enter your password")
        if websiteask == "y":
            websitein = input("website name: ")
            password = input("enter your password")
            print("Your website is", websitein, "your password is:", password)
        if websiteask == "n":
            print("your password is:", password)
        saves = input("save?")
        if saves == "y" and websiteask == "y":
            f = open("pass.txt", "a")
            f.write("website name: ")
            f.write(websitein)
            f.write("\n")
            f.write("password: ")
            f.write(password)
            f.write("\n\n")
            f.close()
            if saves == "y" and websiteask == "n":
                f = open("pass.txt", "a")
                f.write("password: ")
                f.write(password)
                f.write("\n\n")
                f.close()
            print("your password text file has been saved in the folder where you have this program located")
            input("press enter to exit")
if menu == "3":
    lowercase =  "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUV"
    numbers = "1234567890"
    symbols = "/:;!@#$%^&*()_+-=\?"
    usefor = lowercase+uppercase+numbers+symbols
    lfp = random.randint(8,32)
    password = "".join(random.sample(usefor, lfp))
    inputs = input("input?: ")
    if inputs == "y":
        websiteask = input("website?: ")
        if websiteask == "n":
            print("ok")
            password = input("enter your password")
        if websiteask == "y":
            websitein = input("website name: ")
            print("Your website is", websitein, "your password is:", password)
        if websiteask == "n":
            print("your password is:", password)
        saves = input("save?")
    if saves == "y" and websiteask == "y":
        f = open("pass.txt", "a")
        f.write("website name: ")
        f.write(websitein)
        f.write("\n")
        f.write("password: ")
        f.write(password)
        f.write("\n\n")
        f.close()
    print("your website and password text file have been saved in the folder where you have this program located")
    if saves == "y" and websiteask == "n":
        f = open("pass.txt", "a")
        f.write("password: ")
        f.write(password)
        f.write("\n\n")
        f.close()
        print("your password text file has been saved in the folder where you have this program located")
        input("press enter to exit")
if menu == "2":
    fe = os.path.exists('pass.txt')
    if fe == True:
        f = open("pass.txt", "r")
        print("\n",f.read())
        input("press enter to exit")
    if fe == False:
        inp = input("sorry, pass.txt does not exist, would you like to make it?\n")
        if inp == "n":
            print("ok")
            input ("press enter to exit")
        if inp ==  "y":
            print("ok")
            f = open("pass.txt", "a")
            f.close()
            input("press enter to exit")
            
