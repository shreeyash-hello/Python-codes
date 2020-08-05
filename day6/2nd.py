def min_max(a,b):
    l=[]
    l.append(a)
    l.append(b)
    return l
a=int(input('enter 1st no: '))
b=int(input('enter 2nd no: '))
ret=min_max(a,b)
print('maximum value is: '+str(max(ret))+'\nminimum value is: ',min(ret))

