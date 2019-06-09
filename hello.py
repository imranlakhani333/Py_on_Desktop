# display
# first letter will be small
print("Hello, world!")
# numbers
print(100)
x = 100
print(x)
# variable can't be a number or start with number
# variable can't have a special character except _
# like _abx or avb_asd
# reserved keywords
# variable can have alpha numeric 
# string operation
string = ("paKistan is a country \n It is in Asia")
print(string.upper())
print(string.lower())
print(string.swapcase())
print(string.title())
print(string.capitalize())
# commenting can be done """
# you can comment multiple selections by ctrl + / and do ctrl + \ to remove them
"""
this is a comment
"""
print(''' We are studying
AI ''')
# variable can't have space
# variable naming
nameofcountry = 1
name_of_country = 2
name_of_city = 3
print(name_of_city)
# syntax means you have not followed guidelines of language
name_of_country = 50
print(name_of_country)
# operations
num = 100
print(num + 10)
num = "abc"
print(num+" 10")
num2 = "500"
print(num2 + "50")
print('''you're my love. "All praises to Allah" ''')
# - and / doesn't work with string. when you write * and a number. it repeats it number of times that number like you 
# write 2 it will write it 2 times.
print(25.5) #flaot - the numbers in decimals
print(10.0123)
print("100"*3)
num4 = 20
num5 = 30
print(num4+num5)
num6 = num5 - num4
print(num6)
num7 = num5*num4
print(num7)
print(num5*3)
print(3*2)
num8 = num5 / num4
print(num8)
print(num5/3)
print(3/2)
# when you divide with single / the answer will be flaot.
print(num5//3)
# when you divide with double // the answer will be integer.
print(3//2)
# Modulo
print(3 % 2)
print(3 % 4)
#TypeCasting
print(int(20.0)) #float to int
# it will not round but truncate it
print(float(50)) #int to float
#
#26 May 2019
#
a = 19
n = 17
c = 20
if True and False:
    print('true')
else:
    print('false')
if 9<6 or 9>3:
    if 5<3 or (3>5 and 15>9):
        print('true')
    elif a==n:
        print("a=n")
    elif c>a:
        print("c>a")
    else:
        print('false')
else:
    print("nested else")
# Elif example
# isCNICValid = input('Do you have CNIC which is not expired? (Please answer in yes / no) ')
# Gender = input('Please specify gender! (Male or Female) ')
# if isCNICValid.lower() == 'yes' and Gender.lower() == 'male':
#     print('Please go to booth A')
# elif isCNICValid.lower() == 'yes' and Gender.lower() == 'female':
#     print('Please go to booth B')
# else:
#     print('Please go home')
#
isCNICValid = input('Do you have CNIC which is not expired? (Please answer in yes or no) ')
if isCNICValid.lower() == 'yes':
    Gender = input('Please specify gender! (Male or Female) ')
    if Gender.lower() == 'male':
        print('Please go to booth A')
    elif Gender.lower() == 'female':
        print('Please go to booth B')
else:
        print('Please go home')
# "!" means not like if ! True means if not true
