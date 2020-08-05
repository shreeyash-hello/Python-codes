import random
while True:
    print('the number on dice is: ',random.randint(1,6))
    again=input('roll again? (y or n): ')
    if again=='y'or again=='Y':
        continue
    else:
        break
