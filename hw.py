class BMW():
    def fuel(self):
        print("Electric")
    def speed(self):
        print("Max of 200kmph")

class Farrari():
    def fuel(self):
        print("Gas")
    def speed(self):
        print("Max of 300kmph")

b = BMW()
f = Farrari()
for car in (b, f):
    car.fuel()
    car.speed()