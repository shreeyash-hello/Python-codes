#  Four integers x,y,z and n, each on a separate line.
#  Print the list in lexicographic increasing order.
# sample input 
#  1
#  1
#  1
#  2

#  sample output
#  [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

list=[]
list1=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                list1=[i,j,k]
                list.append(list1)

print(list)


