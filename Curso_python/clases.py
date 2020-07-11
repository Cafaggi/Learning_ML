class rectangle:
    def __init__ (self, width, heigth):
        self._width = width
        self._heigth = heigth
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def heigth(self):
        return self._heigth

    @heigth.setter
    def heigth(self, heigth):
        self._heigth = heigth

    def area(self):
        return self.width * self.heigth
    
    def __repr__(self):
        #how to construct the object
        return 'rectangle ({0} , {1})'.format(self.heigth,self.heigth)
    
    def __str__(self):
        #how to represent the object
        return 'rectangle width = {0}, heigth {1}'.format(self.heigth,self.heigth)

    def __lt__ (self, other):
        #lower than
        return self.area() > other.area()

r1 = rectangle(10,20)
r2 = rectangle(10,30)

print(r1, r1.area(), str(r1), r1>r2)