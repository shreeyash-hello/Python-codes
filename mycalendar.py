import calendar
while True:
    y = int(input("Input the year (YYYY) : "))
    year_length=len(str(y))
    if year_length>4:
        print('enter appropriate year : ')
    elif year_length==4:
         break
while True:
    try:
        while True:
            m = int(input('Input the month (MM) : '))
            month_length=len(str(m))
            if month_length>2:
                print('enter appropriate month ')
            elif month_length==2:
                print(calendar.month(y, m))
                break
    except IndexError:
        print('no such month exists')
        False
