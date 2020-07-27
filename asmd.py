a=input('what operation you want ?\n1.addition(+)\n2.multiplication(*)\n3.subtraction(-)\n4.division(/)\n')
num1=int(input('enter the number 1 : '))
num2=int(input('enter the number 2 : '))
if a=='1':
    print('the addition is :',num1+num2)
elif a=='2':
    print('the multiplication is : ',num1*num2)
elif a == '3':
    if (num1>num2):
        print('the subtraction is : ', num1 - num2)
    else:
        print('cannot perform operation')
elif a=='4':
    if  num2==0:
        print('cannot perform')
    else:
        print('the division is : ',num1/num2)
else:
    print('choose appropriate choice')
