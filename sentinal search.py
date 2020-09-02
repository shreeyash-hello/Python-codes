list=[]
n=int(input('enter number of students: '))
for i in range(n):
    roll=int(input('enter the roll nos: '))
    list.append((roll))

f=int(input('enter the roll no to search: '))
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==f:
            return True
        i=i+1
    return False
if search(list,f):
    print('roll number found')
else:
    print('not found')




