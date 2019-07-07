# def givemesomecalculation(number1):
#     def innercalculation():
#         return number1 * 4
#     return innercalculation()
# print(givemesomecalculation(6))
# def givemesomecalculation(number1, which):
#     def innercalculation():
#         return number1 * 4
#     def innercalculation2():
#         return number1 + 4
#     if which == "innercalculation":  
#         return innercalculation()
#     else:
#         return innercalculation2()
# print(givemesomecalculation(6,"innercalculation"))
# read: r 
# write: w 
# append: a
# with open('textfile.txt',"w") as file:
    # print(file.writable())
    # file.write("Name\n")
    # file.write("Imran\n")
    # file.write("Ismail\n")
    # file.write("Sauleh\n")
    # file.writelines("Ali")
# with open('textfile.txt',"a") as file:
    # print(file.writable())
    # file.write("Imran\n")
    # file.write("Ismail\n")
# with open('textfile.txt',"r") as file:
    # for line in file:
        # print(line)
        # print(line.rstrip())
# print(file.readlines())
    # print(file.read())
    # line1 = file.readline()
    # line2 = file.readline()
    # print(line1)
    # print(line2)
    # print(file.readlines()[1])
    # element=file.readlines()[1]
    # print(element.rstrip())
    # a = element.rstrip()
    # print(a.strip())
# flie = open('textfile.txt','r')
# print(flie.read())
# flie.close()
# flie = open('textfile.txt','w')
# flie.write('ABC')
# flie.close()
# def (a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# class Student():
#     def __init__(self):
#         pass
#     def printname(self):
#         print("Function Name")
# import csv
# with open('data.csv','r') as fd:
#     csv_reader = csv.reader(fd)
#     for line in csv_reader:
#         print(line)
# path = input('Enter path to store file: ')
# with open('data.csv',"w",newline="") as fd:
#     csv_writer =csv.writer(fd,delimiter=',')
#     csv_writer.writerow(["Name","Age","Class"])
#     csv_writer.writerow(["Imran",32,"Father"])
#     csv_writer.writerow(["Ismail",63,"Grand Father"])
#     csv_writer.writerow(["Sauleh",4,"Son"])
# import json
# student = {
#     "Name":"Imran",
#     "Age":32,
#     "Class":"AI"
# }
# with open("data.json","w") as fd:
#     json.dump(student, fd)
# import json
# student = {
#     "Name":"Imran",
#     "Age":32,
#     "Class":"AI"
# }
# with open("data.json","r") as fd:
#     student = json.load(fd)
#     print(student)
    # json.dump(student, fd)
import json
student = {
    "Name":"Imran",
    "Age":32,
    "Class":"AI"
}
try:
    print(10/0)
    with open("C:\\data.json","r") as fd:
        student = json.load(fd)
        print(student)
except FileNotFoundError:
    print("Please Check. File does not exist on specified location")
except:
    print("An un-known error has occurred")
# Student Management System
# Dictionary
