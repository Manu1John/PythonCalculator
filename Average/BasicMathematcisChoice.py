n1 = int(input("Enter Two Numbers"))
n2 = int(input(""))
print("1 for Addition \n2 for Subtraction \n3 for Division \n4 for Multiplication \n Enter Your Choice")
Choice = int(input(""))
if (Choice == 1):
    R = n1 + n2
    print("Result is " + str(R))
elif (Choice == 2):
    R = n1 - n2
    print("Result is " + str(R))
elif (Choice == 3):
    R = n1 / n2
    print("Result is " + str(R))
elif (Choice == 4):
    R = n1 * n2
    print("Result is " + str(R))
else:
    print("You are Fucked")
