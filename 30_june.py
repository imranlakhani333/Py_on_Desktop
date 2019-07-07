# def adder(*numbers):
#     constant = 2*9.81*3.147
#     def inner():
#         total = 0
#         for number in numbers:
#             total += number
#         print(numbers)
#         print(total)
#         return constant * total
#     return inner
# # adder_fn = adder 
# # adder_fn(1)
# # adder_fn(1,5)
# # adder(1,7,2)
# inner_fn = adder(2,4)
# print(inner_fn)
# constant = 0
# lst =[0,2,4]
# def adder(*numbers):
#     lst =[]
#     lst.append(1)
#     constant = 2*9.81*3.147
#     def inner():
#         total = 0
#         for number in numbers:
#             total += number
#         print(numbers)
#         print(total)
#         return constant * total
#     return inner
# inner_fn = adder(2,4)
# print(constant)
# print(lst)
# lst = [1,2,3,4,5,6]
# print('for loop')
# for number in lst:
#     print(number)
# print('while loop')
# idx = 0
# while idx < len(lst):
#     print(lst[idx])
#     idx+=1
class Patient():
    def __init__(self,name,age,cnic,father_name = "not specified"):
        print("I am a constructor")
        self.name = name
        self.age = age
        self.cnic = cnic
        self.father_name = father_name
        self.location = "Karachi"
        self.__abc = "Lahore"
    def describe_full_name(self):
        print(f'{self.name} {self.father_name}')
    def age_increment(self,inc_val):
        self.age+=inc_val

new_patient = Patient("Hamza" , 25 , "4210163822557","Arshad")
print(new_patient.location)
# print(new_patient.__abc)
# print(new_patient.age)
# new_patient.age_increment(2)
# new_patient.age = 28
# print(new_patient.age)
# new_patient.describe_full_name()
# new_patient_2 = Patient("Osama", 30, "4210163822558","Not Specified")
# new_patient_2.describe_full_name()
# print(new_patient.name)
# print(new_patient_2.name)
# new_patient.father_name = "Arshad"
# print(new_patient.father_name)