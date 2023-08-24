import qrcode
from tkinter import *

def qrmaker(object_name,link,):
    created_qr = qrcode.make(f"{link}")
    created_qr.save(f"{object_name}.png")


# object_name = input('Enter The object name ')
# link = input('paster Your link here to generate qrcode ')

# qrmaker(object_name,link)
# print('Your qu create successfully !')


# gui = Tk()
# gui.title('qr code generator 👻🧑‍💻')
# gui.geometry('500x500')
# object_name = Label(gui, text='Object Name')
# object_name.place(x=20,y=20)
# inputeobject = Entry(gui)
# inputeobject.place(x=70,y=20)
# gui.mainloop()


# num1 = 4
# num2 = 3
# num3 = 2

# myList = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(myList)):
#         if i%2 == 0:
#             print(myList[i])

# friend dictionary
# class frined(name, mobile):
# print (" Learning Exceptions...")
# # try:
# num1= int(input ("Enter the first number"))
# num2=int(input("Enter the second number"))
# quotient=(num1/num2)
# ans = isnumeric()

# except type(num1): # to enter only integers
#     print (" Please enter only numbers")
#
# except ____________: # Denominator should not be zero
#    print(" Number 2 should not be zero")
#
# else:
#     print(" Great .. you are a good programmer")
#
#  ___________: # to be executed at the end
#     print(" JOB OVER... GO GET SOME REST")

# table = int(input('enter which table you want:'))
# for i in range(1,11):
#     print(i*table)


import tkinter as tk

def calculate_average(*nums):
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1
    avg = total / count
    return avg

numbers = [10, 20, 30, 40, 50]
print(calculate_average(*numbers))


# let's create gui

"""
 
 
 ------------------------D E V E L O P E D   B Y    P R A N A V    S I R S U F A L E ---------------------


"""