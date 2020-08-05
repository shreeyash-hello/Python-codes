import math
def co_ordinates(x1,y1,x2,y2):
    l1=[]
    l2=[]
    l1.append(x1)
    l1.append(y1)
    l2.append(x2)
    l2.append(y2)
    distance = math.sqrt(((l1[0] - l2[0]) ** 2) + ((l1[1] - l2[1]) ** 2))
    return distance
while True:
    a=float(input('enter x1: '))
    b=float(input('enter y1: '))
    c=float(input('enter x2: '))
    d=float(input('enter y2: '))
    ans=co_ordinates(a,b,c,d)
    print('the distance of the co-ordinates are: ',ans)
    again=input('do you want to enter again? (y or n): ')
    if again=='y'or again=='Y':
        continue
    else:
        break
