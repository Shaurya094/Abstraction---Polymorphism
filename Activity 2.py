from abc import ABC, abstractmethod
class ani(ABC):
    def move(self):
        print ("I can fly")

class hum(ani):
    def move(self):
        print("I can build")
class python(ani):
        def move(self):
             print ("I can code")
class dog(ani):
         def move(self):
             print("I can bark")
class lion(ani):
         def move(self):
             print("I can roar")

h = hum()
p = python()
d = dog()
l = lion()
l.move()
h.move()
p.move()
d.move()
