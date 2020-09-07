#Find out the length of the minimum subarray whose sum is greater than or equal to the given number.


def smallSumSubset(data, target, maxVal):
    
    if target <= 0:
        return 0
    elif sum(data) < target:
        return maxVal
    elif sum(data) == target:
        return len(data)
    elif data[0] >= target:
        return 1

    elif data[0] < target:
        return min(smallSumSubset(data[1:], target, maxVal), \
                   1 + smallSumSubset(data[1:], target - data[0], maxVal))

inp=int(input('enter the number of values you want in array: '))
data=[]
for i in range(inp):
    inp1=int(input(f'enter array element {i+1}: '))
    data.append(inp1)
target = int(input('enter the target sum: '))

val = smallSumSubset(data, target, len(data) + 1)

if val > len(data):
    print(-1)
else:
    print('the min length of sub-array is: ',val)
