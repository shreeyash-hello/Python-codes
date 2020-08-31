def selection_sort():
    A = []
    inp = int(input('enter the number of students: '))
    for i in range(inp):
        enter = float(input(f'enter the percentage of student {i + 1}: '))
        A.append(enter)

    for i in range(len(A)):
        # print(A)
        a = i
        for j in range(i + 1, len(A)):
            if A[a] > A[j]:
                a = j
        A[i], A[a] = A[a], A[i]

    print("Sorted array in selection sort is: ", A)

    print('first five greatest marks: ',A[::-1])


def bubble_sort():
    A = []
    inp = int(input('enter the number of students: '))
    for i in range(inp):
        # print(A)
        enter = float(input(f'enter the percentage of student {i + 1}: '))
        A.append(enter)

    n = len(A)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    print("Sorted array in bubble sort is: ", A)

    print('first five greatest marks: ',A[::-1])

def main():
    bubble_sort()
    selection_sort()

if __name__=='__main__':
    main()

