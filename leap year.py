
while True :
    year = int(input("Enter year to be checked:"))
    string = str(year)
    length = len(string)
    if length == 4:
        if(year%4==0 and year%100!=0 or year%400==0):
            print("The year is a leap year!")
            break
        else:
            print("The year isn't a leap year!")
            break
    else:
        print('enter appropriate year')
