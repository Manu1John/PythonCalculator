class FirstClass:
    def __init__(self):
        print("Welcome to CrossRoads")
    def Set_name(self,name):
        self.name=name
    def Set_Place(self,place):
        self.place=place




    def Set_Age(self,age):
        self.age=age
    def Add_Age(self):
        self.age=self.age+1

class SecondClass(FirstClass):
    def __init__(self):
        print("How far we Can go")
        super().__init__()


    def Display(self):
        print("Candidate Name ")


    def Show_Place(self):
        print("Place :"+self.place)
    def Show_name(self):
        print("Name :"+self.name)
    def Show_age(self):
        print("Age :"+str(self.age))


S=SecondClass()
S.Display()
S.Set_name("Manu John")

S.Set_Age(22)
S.Show_age()
S.Set_name("Ajmal")
S.Show_name()

S.Set_Place("Canada")
S.Show_Place()
