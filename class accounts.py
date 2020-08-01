#Create classes that capture bank customers and bank accounts. A customer has a first and last name. 
#An account has a customer and a balance. Make objects for two accounts held by the same customer.

class bank:
    def account(self,acc_name,name_of_costumer,last_name):
        self.acc_name=acc_name
        self.name_of_costumer = name_of_costumer
        self.last_name=last_name
        print('The account number is : '+str(acc_name)+'\nthe name of costumer is : ',name_of_costumer,last_name)

obj1=bank()
n=int(input('enter the number of accounts you want to access : '))
for i in range(n):
    ac=int(input('enter account number : '))
    nm=input('enter first name : ')
    ln=input('enter last name : ')
    obj1.account(ac,nm,ln)
