from abc import ABC, abstractmethod
class Abc(ABC):
    def print(self, x):
        print ("Passed value: ", x)


        def task(self):
            print ("We're inside Abc's task")

class test(Abc):
    def task (self):
        print("We're inside test's class")

test_obj = test()
test_obj.task()
test_obj.print(100)