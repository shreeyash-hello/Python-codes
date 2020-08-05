def items(price):
    discount=price*20/100
    final_price=price-discount
    return final_price
while True:
    rs = float(input('enter the item price: '))
    while True:
        if rs<=0.05:
            print('not accepted')
        else:
            break
    item=items(rs)
    if rs>0.05:
        print('the price after discount is: Rs',item)
    again=input('add another item? (y or n): ')
    if again=='y' or again=='Y':
        continue
    else:
        print('thank you')
        break







