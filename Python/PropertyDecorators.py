class Student:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Start Deleting")
        self.first = None
        self.last = None


obj = Student("Surenthar", "S")

obj.first = "Kamal"
# obj.fullname = "Bala Murugan"

print(obj.first)
print(obj.last)
print(obj.email())
# print(obj.fullname)

# del obj.fullname
