"""menu-driven python application with following menu options for users"""
from datetime import date
import random
import math
i = 0
#This would be input form user and print of the menu on command line
while i != 6:
    print("Enter 1 for the Password Generator")
    print("Enter 2 Calculate and Format Percentage")
    print("Enter 3 How many Days from Today until July 4, 2025")
    print("Enter 4 Use the law of cosine to calculate the leg of a triangle")
    print("Enter 5 Calculate the volume of a right circular cylinder")
    print("Enter 6 to exit the program")
    #input of choice by user
    Inp = int(input("Enter a choice: "))
    if Inp == 6:
        # exit message thanking the user
        print("Thank You for using Nicolai's Security, Have a good day!")
        break
        #for input selection for password
    elif Inp == 1:
        #questions for user to tailor the password security for user
        L = int(input("Enter the length of the password: "))
        Num = int(input("Enter 0 if no NUMBERS are needed in the password or enter 1:  "))
        Up = int(input("Enter 0 if no UPPER CASE LETTERS are needed in the password or enter 1:  "))
        Low = int(input("Enter 0 if no LOWER CASE LETTERS are needed in the password or enter 1: "))
        Spe = int(input("Enter 0 if no SPECIAL CHARACTERS are needed in the password or enter 1: "))
        PASSWORD = ""
        Dic = []
        #the function of the program to create the password with the user selected input
        if Num == 1:
            X = chr(random.randint(48,57))
            PASSWORD = PASSWORD + X
            L -= 1
            if L < 0:
                print("invalid input")
                continue
            Dic.append([48, 57])
        if Up == 1:
            X = chr(random.randint(65, 90))
            PASSWORD = PASSWORD  + X
            L -= 1
            if L < 0:
                print("invalid input")
                continue
            Dic.append([65, 90])
        if Low == 1:
            X = chr(random.randint(97, 122))
            PASSWORD = PASSWORD  + X
            L -= 1
            if L < 0:
                print("invalid input")
                continue
            Dic.append([97, 122])
        if Spe == 1:
            X = chr(random.randint(33, 46))
            PASSWORD = PASSWORD  + X
            L -= 1
            if L < 0:
                print("invalid input")
                continue
            Dic.append([33, 46])
        for i in range(L):
            R = random.randint(0, len(Dic) - 1)
            PASSWORD = PASSWORD + chr(random.randint(Dic[R][0], Dic[R][-1]))
        PASSWORD = ''.join(random.sample(PASSWORD, len(PASSWORD)))
        #final product of the tailored password for user, and prints out unique password
        print(f"the generated password is {PASSWORD}.")
        #selection for calculating and formulating percentages
    elif Inp == 2:
        Num = float(input("Enter the numerator: "))
        Denom = float(input("Enter the denominator: "))
        Decimal = int(input("Enter the number of decimal points for formatting: "))
        # equation fomulated and excuted by the progam and user input
        Val = Num/Denom*100
        Val = round(Val, Decimal)
        # print of final production of the users inputted values and equation excution
        print(f"Percentage value is {Val}.")
        #date and time selection from the menu
    elif Inp == 3:
        D0 = date.today()
        D1 = date(2025, 7, 25)
        Delta = D1 - D0
        #print of the days left from the pre programmed date
        print(f"Total number of days are {Delta.days}.")
        #selection for the law of cosine to calculate the leg of a triangle
    elif Inp == 4:
        A = int(input("Enter first side length: "))
        B = int(input("Enter second side length: "))
        Ang = int(input("Enter the angle: "))
        #equation for the user inputted values
        C = A*A + B*B - 2*A*B*math.cos(math.pi/180*Ang)
        #excuted and final calculated value by the user input and progammed equation
        print(f"The leg of the triangle is {C}.")
    else:
        #Calculate the volume of right circular cylinder
        R = int(input("Enter the radius: "))
        H = int(input("Enter the height of cylinder: "))
        #progammed equation
        Vol = math.pi*R*R*H
        #print of final value from user input and the calculated value
        print(f"Volume of the cylinder is {Vol}.")
    print()
    print()
    