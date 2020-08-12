inp=input('enter the string: ')
char = inp[0]
inp = inp.replace(char, '$')
inp = char + inp[1:]
print(inp)
