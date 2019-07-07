# loops
# for x in range(5):
#     print("Imran")
# for x in range(1,11): 
# #- it prints difference i.e. 11-1 = 10
#    print("2 x "+ str(x) + " = " + str(2*x))
# for x in range(1,11):
#     print(x, end=", ")
# # you write whatever you need between 2 values x in the "end" function
# for x in range(1,6):
#     print(x*"*")
# lst = range(1,51)
# iter = 0
# for x in lst:
#     if iter == len(lst) - 1:
#         print(x * 2)
#     else:
#         print(x*2, end=", ")
#     iter += 1
# for num in range(101):
#     if num % 2 == 0:
#         print(num, end=" ")
# print(" ")
# for numb in range(2, 101, 2):
#     print(numb, end=" ")
# lst = list(range(10,0,-1))
# print(lst)
# task for home = check if number is prime or not in input
# List and functions
# n = [1,2,3,4,5,6,7]
# print("n = " + str(n))
# n.append(8)
# print("after append n = " + str(n))
# n.insert(2,2.5)
# print("after insert n = " + str(n))    
# del n[2]
# print("after delete n = "+str(n))
# n.insert(2,7)
# print("after adding 7 now n = "+ str(n))
# n.remove(7)
# print("after remove n = " + str(n))
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(numbers[3])
# print(numbers[-5])
# for i in range(len(numbers)):
#     print(i, end=" ")
# print(numbers[i], end=" ")
# The above will take value of i like "0" and see whats the value of numbers in that index. In this case its "1".
# print(len(numbers))
# list is group of data
# len is used to determine length of list. Index is always n-1. Starts from 0 and ends n-1.
# hetro_list = ["Imran",1,2.5,True]
# print(hetro_list[2])
# hetro_list[2]=3.5
# print(hetro_list[2])
#            0      1    2      3
# list_1 = ["my","name","is","imran"]
#          -4,   -3,   -2,   -1
# print(list_1[-2])
# odd_numbers = [1,3,5,7,9,11,13]
# length_odd = len(odd_numbers)
# for i in range(length_odd):
#     print(i, end=" ")
# range will simply take length and make a list starting from 0 till number of elements
# a = [1,2,3,4,5,6]
# b = a
# b.append('10')
# print('elements of a', a)
# print('elements of b', b)
# when you equate new list with an existing list. Changes in new list will also be made on existing list.
num_list1 = ['my', 'name','is','Imran','is']
# for i in num_list1:
#     if i=='is':
#         num_list1.remove('is')
# print(num_list1)
# print(num_list1.index('is'))
del num_list1[3]
print(num_list1)
