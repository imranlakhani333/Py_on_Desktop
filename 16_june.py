# # list slicing
# a = [1,2,4,6,-1,-2,100]
# # b = []
# # for i in range(2,6):
# #     b.append(a[i])
# # print(a)
# # print(b)
# # start from element to start and end at one additional element. You want 5th element so type 6.
# # b = a[2:6]
# # print(a)
# # print(b)
# # p = "Pakistan"
# # print(p[2:6])
# b = a[2:6:2]
# print(b)
# Tuples: same as list just have one difference. It's immutable. Can't be changed.
# mutable = something which can be changed
# immutable = which can't be changed
# my_tuple = (1,'hello',55,'hello')
# print(my_tuple)
# print(my_tuple[1])
# print(my_tuple[1:4])
# del my_tuple[0] - can't delete
# my_tuple.append("last value") - can't add any value
# print(my_tuple.index("hello"))
# print(my_tuple.count("hello"))
# print(my_tuple.index("hello",2))
# nested loop
# my_list = ["karachi","lahore","islamabad","Peshawar"]
# # for abc in my_list:
# #     print(abc)
# # n = [1,2,3,4,5,6,7,8,9,10]
# # n1 = []
# # for x in range(1,11):
# #     n1.append(x*2)
# # print(n1)
# #nested loop
# for i in my_list:
#     for x in range(5):
#         print(i,x)
# inner loop executed for each outer loop value
a = int(input("Enter Starting Value: "))
b = int(input("Enter Ending Value: "))
for i in range(a,b+1):
    for x in range(1,11):
        print(str(i)+" x "+str(x)+" = "+str(i*x))