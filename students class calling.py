#Create a class that captures students. Each student has a first name, last name, class year, and major. Create two examples of students.


class students:
    def __init__(self,name,surname,class_year):
        self.name=name
        self.surname=surname
        self.class_year = class_year
        print('name = '+name+'\nsurname = '+surname+'\nclass_year = ',class_year)

n=input('enter first name : ')
s=input('enter last name : ')
cy=input('enter class year : ')
obj=students(n,s,cy)
print(obj.__init__(n,s,cy),obj.__init__(n,s,cy))


