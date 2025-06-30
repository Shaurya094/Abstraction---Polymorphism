class sq:
    def __init__(self, side):
        self.side = side
    def area(self):
        print ("Square's area: ", self.side**2)

class cir:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print ("Circle area: ", 3.14*self.radius * self.radius)

sqr = sq(5)
circ = cir(5)

for shape in (sqr, circ):
    shape.area()