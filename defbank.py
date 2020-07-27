global balance
balance=0

while True:

    transac=input('enter the transaction (e to exit) : ')
    list = transac.split()
    a=list[0]

    if a=='d'or a=='D':

        b = int(list[1])
        balance=balance+b
        print('the new balance is Rs.',balance)
        list.append(transac)
    if a=='w'or a=='W':
        b=int(list[1])
        balance=balance-b
        print('the new balance is Rs.',balance)

    if  transac=='e':
        print('thank you')
        break

