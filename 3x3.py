def read(mat):
    for i in range(3):
        a=[]
        for j in range(3):
            a.append(int(input()))
        mat.append(a)

def matrix(mat):
    print('the matrix is ')
    for i in range(3):
        for j in range(3):
            print(mat[i][j],end=' ')
        print()


def main():
    mat1 = []
    print('enter the elements of matrix: ')
    read(mat1)
    matrix(mat1)

if __name__=='__main__':
    main()

