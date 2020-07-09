class Apple:
    def display(self):
        print("A class")


class Banana:
    def display(self):
        print("B Class")


class Cat(Banana,Apple):
    def display_c(self):
        print("C Class")

C=Cat()
C.display()
print(Cat.mro())