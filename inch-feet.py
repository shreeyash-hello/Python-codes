class addDistance:
    n = int(input('enter'))
    inches=[]
    feet=[]

    for i in range(1,n+1):
        inp_inch=int(input(f'enter inch-({i}) input'))
        inches1=str(inp_inch)
        inches.append(int(inches1))

        inp_feet = int(input(f'enter feet-({i}) input'))
        feet1 = str(inp_feet)
        feet.append(int(feet1))

    total_inch=sum(inches)
    total_feet=sum(feet)
    print(total_inch)
    print(total_feet)


obj1=addDistance()



