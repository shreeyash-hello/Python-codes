def accept_array(arr):
    n=int(input('enter total number of students: '))
    # A.sort(reverse=True)
    for i in range (n):
        x=int(input('enter roll numbers of student %d: '%(i+1)))
        arr.append(x)
    return n

def display_array(arr,n):
    if(n==0):
        print('no records')
    else:
        print('student rolls are: ',end=' ')
        for i in range(n):
            print('%d'%arr[i],end=' ')
        print('\n')

def recursive(arr,low,high,x):
    if (low<=high):
        mid=int((low+high)//2)
        if (arr[mid]==x):
            return mid
        else:
        # mid = int((low + high) // 2)
            if(x<arr[mid]):
                return recursive(arr,low,mid-1,x)
            else:
                return recursive(arr,mid+1,high,x)
    return -1

def iterative(arr,n,x):
    s=0
    l=n-1
    while(s<=l):
        mid=int((s+l)//2)
        if (arr[mid]==x):
            return mid
        else:
            if (x<arr[mid]):
                l=mid-1
            else:
                s=mid+1
    return 0

arr=[]
n=accept_array(arr)
# print(n)
display_array(arr,n)

inp=input('enter which operation (r or i): ')
if inp=='r' :
    find = int(input('enter number to be searched: '))
    flag = recursive(arr, 0, n-1 , find)
    if (flag==-1):
        print('roll number not found')
    else:
        print('roll number found at loaction%d\n'%(flag+1))
if inp=='i' :
    find = int(input('enter number to be searched: '))
    flag2 = iterative(arr, n, find)
    if (flag2 == 0):
        print('roll number not found')
    else:
        print('roll number found at loaction%d\n' % (flag2 + 1))
