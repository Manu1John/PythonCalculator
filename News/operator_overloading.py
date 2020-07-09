class Sample:
    def set_name(self, name):
        self.name = name

    def __add__(self, second):
        name = self.name + second.name
        return name

    def __iadd__(self, other):
        name = self.name + other
        return other


first_name = Sample()
second_name = Sample()
third_name = Sample()
forth_name = Sample()
first_name.set_name("Manu ")
second_name.set_name("John")
third_name.set_name("Ben ")
forth_name.set_name("Jackson")
Final_name = first_name + second_name
print(Final_name)
Last_name = third_name + forth_name
print(Last_name)
