class rectangle:
    def setDim(self,length,breadth):
        self.length=length
        self.breadth=breadth
        return length,breadth

    def getarea(self):
        self.area=self.length * self.breadth
        print('the area of rectangle is : ',self.area)

obj1=rectangle()
l=int(input('enter length(cm) : '))
b=int(input('enter breadth(cm) : '))
obj1.setDim(l,b)
obj1.getarea()