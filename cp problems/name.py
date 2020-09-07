#You are given the firstname and lastname of a person on two different lines. Your task is to read them and print.


def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))
    return a,b

if __name__ == '__main__':
    print('enter the first and last name\n')
    first_name = input()
    last_name = input()

print_full_name(first_name, last_name)
