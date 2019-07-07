# # Dictionaries Chapter 25
# # use curly brackets
# # if the attribute is string use inverted comma
# student = {"Name": "Imran", "Father_Name": "Ismail", "age": 32}
# # give name of key to print in dictionaries
# # print(student["Name"])
# # to check if key exist
# # print('F Name' in student)
# # student["Number of Children"] = 3
# # print(student["Number of Children"])
# # for i in range(5):
# #     if "FName" in student:
# #         print("FName" in student)
# #     else:
# #         print("FName does not exist")
# # my_key = "Contact Number"
# # print(student.keys())
# # print(student.values())
# # print(student.items())
# for value in student.values():
#     print(value)
# for k, v in student.items():
#     print(k, v)
# tpl =(2,4,6)
# a,b,c = tpl
# print(a)
# print(b)
# print(c)
# x = [2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59]
# for i in range(100):
#     if i % 2 == 0:
#         continue
#     else:
# #         print(i)
# for i in range(0,10):
#     if i % 2 == 0:
#         break
#     else:
#         print(i)
# students = []
# while True: 
#     print("Press 1 to Add Student")
#     print("Press 2 to Delete Student")
#     print("Press 3 to Search Student")
#     print("Press 4 to Edit Student")
#     print("Press 5 to Print Student")
#     print("Press 6 to Exit")
#     option = input("Enter 1 - 5: ")
#     if option == "6":
#         break
#     elif option == "5":
#         print(students)
#     elif option == "1":
#         student = {}
#         student["Name"] = input("Student Name: ")
#         student["Father Name"] = input("Student Father Name: ")
#         student["Address"] = input("Student Address: ")
#         students.append(student)
#     elif option == "2":
#         Name = input("Enter the name of Student you want to delete: ")
#         ind = 0
#         for student in students:
#             if student['Name'] == Name:
#                 del students[ind]
#                 break
# #             ind+=1
# lst = [
#     {
#         'Name':"Imran"
#     },
#     {
#         "Name":"Sauleh"
#     },
#     {
#         "Name":"Safa"
#     }
# ]
# print(lst[1]['Name'])
# employee = {
#     "Name": "Imran",
#     "F Name":"Ismail",
#     "Child":{
#         "Name": "Ilma"
#     }
# }
# print(employee["Child"]["Name"])
# employee = {
#     "Name": "Imran",
#     "F Name":"Ismail",
#     "Projects":['Job','Proxy Marketing','AI class','Father and Husband'],
#     "Child":[
#     {
#         "Name": "Sauleh"
#     },
#     {
#         "Name":"Ilma"
#     },
#     {
#         "Name":"Safa"
#     }]
# }
# # print(employee["Projects"][-1])
# print(employee["Child"][-1]["Name"])
# def arithmetic_operations(operand1, operand2=0, operator="+"):
#     # print("Hello I am inside a function")
#     if operator == '+':
#         print(operand1 + operand2)
#     if operator == '*':
#         print(operand1 * operand2)
# print("Hello I am OUTSIDE a function")
# arithmetic_operations(2,3,'*')
# arithmetic_operations(2,3)
# arithmetic_operations(2)
# arithmetic_operations(2, operator='*')
# def function_with_variable_args(*all_params):
#     print(all_params)
# function_with_variable_args(1)
# function_with_variable_args(1,2)
# function_with_variable_args(1,2,True)
# def function_with_variable_args(**all_params):
#     print(all_params)
# function_with_variable_args(Name = "Imran")
# function_with_variable_args(Name = "Imran", FName = "Ismail")
# function_with_variable_args(Name = "Imran", FName = "Ismail", Age = "32")
# set can't have repeated value. it's also in curly brackets.
s = {1,2,3,4,5,6}