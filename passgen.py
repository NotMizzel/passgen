print("password generator. y or n for all prompts")
import random
lowercase =  "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUV"
numbers = "1234567890"
symbols = "/:;!@#$%^&*()_+-=\?"
usefor = lowercase+uppercase+numbers+symbols
lfp = random.randint(8,32)
password = "".join(random.sample(usefor, lfp))
inputs = input("make new?")
if inputs == "y":
    websiteask = input("website?")
    if websiteask == "n":
        print("ok")
    if websiteask == "y":
        websitein = input("website name")
        print("Your website is", websitein, "your password is:", password)
    if websiteask == "n":
        print("your password is:", password)
    saves = input("save?")
if saves == "n" and websiteask == "y":
    input("press enter to exit")
if saves == "n" and websiteask == "n":
    input("press enter to exit")
if saves == "y" and websiteask == "y":
    f = open("pass.txt", "w")
    f.write("website name: ")
    f.write(websitein)
    f.write("\n")
    f.write("password: ")
    f.write(password)
    f.close()
    print("your website and password text file have been saved in the folder where you have this program located\nmove the file to another location or it will be overwritten")
    input("press enter to exit")
if saves == "y" and websiteask == "n":
    f = open("pass.txt", "w")
    f.write(password)
    f.close()
    print("your password text file has been saved in the folder where you have this program located\nmove the file to another location or it will be overwritten")
    input("press enter to exit")
