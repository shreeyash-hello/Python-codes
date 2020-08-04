number_array = list()
number = input("Enter the number of elements you want: ")
print ('Enter numbers in array: ')

for i in range(int(number)):
    n = input(f"number {i+1} : ")
    number_array.append(int(n))

print('original array is: ',number_array)
print ('circulatory right array is: ',number_array[::-1])
