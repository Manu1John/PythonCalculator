num = int(input("Enter a Number"))
b = int(input("Enter Division number"))
R=str
try:
    R=num/b
    print(R)
    print("Try Completed")
except ZeroDivisionError:
    print("Can't Divided by Zero")
    print("Programme Comple")