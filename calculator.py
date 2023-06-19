n1=int(input("enter operand 1: "))
n2=int(input("enter operand 2: "))
print(" 1)Addition\n 2)Subtraction\n 3)Multiplication \n 4)Division")
o1=int(input("enter mode of calculation: "))
if (o1 == 1): 
    print("Addition= ",n1+n2)
elif o1==2:
    print("Subtraction= ",n1-n2)
elif o1==3:
    print("Multiplication= ",n1*n2)
elif o1==4: 
    print("Division ",n1/n2)
else:
    print("enter correct option")
