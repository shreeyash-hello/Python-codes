def read(r,c,mat):
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(int(input()))
        mat.append(a)

def dis(r,c,mat):
    for i in range(r):
        for j in range(c):
            print(mat[i][j],end=' ')
        print()

def sparse_conversion(r,c,mat,s):
    a = [r,c,0]
    nt = 0

    s.append(a)
    for i in range(r):
        for j in range(c):
            if mat[i][j] != 0:
                a=[i,j,mat[i][j]]
                s.append(a)
                nt+=1
    s[0][2] = nt


def dis_sparse(s,str):
    print('%s sparse matrix is: '%str)
    print('\t\t   row    col    val ')
    print('\t\t |%4d |%4d |%4d |'%(s[0][0],s[0][1],s[0][2]))
    print('\t\t -------------------')
    for i in range(1,s[0][2]+1):
        print('\t\t |%4d |%4d |%4d |' % (s[i][0], s[i][1], s[i][2]))

def trans(s,t):
    a=[s[0][1],s[0][0],s[0][2]]
    t.append(a)
    for i in range(s[0][1]):
        for j in range(1,s[0][2]+1):
            if(s[j][1]==i):
                a=[s[j][1],s[j][0],s[j][2]]
                t.append(a)



def main():

    r=int(input('enter the rows of matrix  : '))
    c=int(input('enter the columns of matrix  : '))

    mat=[]

    print('enter the elements of matrix ')
    read(r,c,mat)

    print('the matrix is: ')
    dis(r,c,mat)

    s=[]
    sparse_conversion(r,c,mat,s)
    dis_sparse(s,'first')

    s1 = []
    trans(s, s1)
    dis_sparse(s1, 'transpose')

if __name__=='__main__':
    main()
