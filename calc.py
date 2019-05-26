num1 = float(input('''Enter 1st number: '''))
num2 = float(input('''Enter 2nd number: '''))
op = input('''Please provide operator (+,-,*,/): ''')

if op == '+':
    print("Result of Adding Numbers "+str(num1)+' and '+str(num2)+' is '+str(num1 + num2))
elif op == '-':
    print("Result of Subtracting Numbers "+str(num1)+" from "+str(num2)+" is "+str(num1 - num2))
elif op == '*':
    print("Result of Multiplicating Numbers "+str(num1)+" with "+str(num2)+" is "+str(num1 * num2))
elif op == '/':
    print("Result of Dividing Numbers "+str(num1)+" from "+str(num2)+" is "+str(num1 // num2)+" and the remainder is"+str(num1 % num2))
else:
    print('Sorry the operation you typed is invalid')
