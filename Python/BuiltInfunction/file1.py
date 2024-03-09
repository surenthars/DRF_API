from file2 import *
import django

# 1)."__all__"  ==>Its using security purpose its which variable allow when we decide

print(name)
print(work)


# 2)."__args__" ==> its represents passing the arguments
class MyClass:
    def __init__(self, *args):
        self.__args__ = args


obj = MyClass(1, 2, 3)
print(obj.__args__)  # Output: (1, 2, 3)

# 3)__add__ ==>its adding value in integer

number = 20
number2 = number.__add__(20)
print(number2)


print(django.__version__)


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_object = MyClass("My Object", 20)

print(my_object.__dict__)  # its return the file


filepath = __file__  # its gives a current path of the file
print("Path to the current file:", filepath)


print(__name__)


print(id(10))
print(id(10))
