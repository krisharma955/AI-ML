# if, elif, else

age1 = int(input("Enter your age: "))
if (age1 >= 18):
    print("you can vote")
else:
    print("you can't vote")

color = input("Enter color: ")
if (color == "red"):
    print("STOP!")
elif (color == "yellow"):
    print("WAIT & LOOK!")
elif (color == "green"):
    print("GO!")
else:
    print("Not a valid traffic light color!")

age2 = int(input("enter your age: "))
if (age2 < 13):
    print("child")
elif (age2 >= 13 and age2 < 18):
    print("teenager")
else:
    print("adult")

username = input("enter username: ")
password = input("enter password: ")
if(username == "admin" and password == "pass"):
    print("Access Granted")
elif(username == "admin" and password != "pass"):
    print("Incorrect password")
elif(username != "admin" and password == "pass"):
    print("Incorrect username")
else:
    print("Incorrect username and password")

n = int(input("enter a number: "))
if(n % 5 == 0):
    print(n, "is a multiple of 5")
else:
    print(n, "is not a multiple of 5")

num = int(input("enter a number: "))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

id = int(input("enter your id: "))
key = input("enter your key: ")
if(id == 1 and key == "one"):
    print("Success")
else:
    if(id == 1 and key != "one"):
        print("Wrong key")
    elif(id != 1 and key == "one"):
        print("Wrong id")
    else:
        print("Wrong id and key")