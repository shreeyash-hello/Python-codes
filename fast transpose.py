def dis_sparse(s,str):
    print('%s sparse matrix is: '%str)
    print('\t\t   row    col   val ')
    print('\t\t |%4d |%4d |%4d |'%(s[0][0],s[0][1],s[0][2]))
    print('\t\t -------------------')
    for i in range(1,s[0][2]+1):
        print('\t\t |%4d |%4d |%4d |' % (s[i][0], s[i][1], s[i][2]))
        
def fast_trans(s,t):
    a = [s[0][1], s[0][0], s[0][2]]
    t.append(a)
    for i in range(s[0][2]):
        t.append([0,0,0])

    x=[]
    for j in range(s[0][1]):
        x.append(0)
    for u in range(1, s[0][2] + 1):
        c=s[u][1]
        x[c]=x[c]+1
    print('frequency array is: ',x)

    pos=[1]

    for c in range(1,s[0][1]+1):
        pos.append(pos[c-1] + x[c-1])
    print('rowStart-pos array: ',pos)
    for i in range(1,s[0][2]+1):
        c=s[i][1]
        k=pos[c]
        t[k][0]=s[i][1]
        t[k][1] = s[i][0]
        t[k][2] = s[i][2]
        pos[c]=pos[c]+1


def main():

    r=int(input('enter the rows of matrix  : '))
    c=int(input('enter the columns of matrix  : '))

    mat=[]

    print('enter the elements of matrix ')
    read(r,c,mat)

    print('the matrix is: ')
    dis(r,c,mat)  

    fast_trans(s,s1)
    dis_sparse(s1, 'fast transpose')

if __name__=='__main__':
    main()      
