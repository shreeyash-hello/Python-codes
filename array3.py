def _findSum(list, N):
    if len(list) == 1:
        return list[0]
    else:

        return list[0] + _findSum(list[1:], N)

n = input('enter the number without any spaces (only one number with no limit of digits): ')
list = [int(d) for d in str(n)]

N = len(list)
ans = _findSum(list, N)
print('the sum of digits are: ', ans)
