class first:
    def __init__(self):
        print("Welcome to Classes")
    def Primary(self):
        print("First Class")
class Second(first):
    def Secondary(self):
        print("Second Class")
class Third(Second):
    def Teritory(self):
        print("Third Class")
Tr=Third()
Tr.Primary()
Tr.Secondary()
Tr.Teritory()
Tr.Primary()