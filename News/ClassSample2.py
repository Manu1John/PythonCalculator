class CrossRoads:
    year=2020
    def __init__(self,n,a,p):
        self.name=n
        self.age=a
        self.place=p
    def add_age(self):
        self.age=self.age+1
    def add_place(self,L):
        self.place=L
    def Display(self):
        print("Year :"+str(CrossRoads.year))
        print("Name :"+self.name)
        print("Age :"+str(self.age))
        print("Place :"+self.place)
    @classmethod
    def add_year(Cls):
        Cls.year=Cls.year+1
    @staticmethod
    def Intro_info():
        print("Welcome")

















x=CrossRoads("Manu John ",22,"Calicut")
y=CrossRoads("Amal Joshy ",21,"Mukkom")


x.Display()
y.Display()
print("--------------------------------")
CrossRoads.add_year()
x.add_age()
y.add_age()
x.add_place("Canada")
y.add_place("Berlin")
CrossRoads.Intro_info()
x.Display()
y.Display()
