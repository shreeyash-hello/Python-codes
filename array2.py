number_array = []

number = input("Enter the number of elements you want: ")
print ('Enter numbers in array: ')

for i in range(int(number)):
    n = input(f"number {i+1} : ")
    number_array.append(int(n))

for i in range(0,len(number_array)):
    number_array[i]=int(number_array[i])
print(number_array)
length=len(number_array)
half_length=len(number_array)//2

part1=number_array[:half_length]
print('1st part of list is: ',part1)

part2=number_array[half_length:]
print('2nd part of list is: ',part2)


