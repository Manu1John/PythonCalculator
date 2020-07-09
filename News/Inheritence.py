class BaseClass:
    def Display(self):
        print("Welcome to")


class SubClass(BaseClass):
    def Balance(self):
        print("New World")


B=BaseClass()
S=SubClass()
B.Display()
S.Balance()