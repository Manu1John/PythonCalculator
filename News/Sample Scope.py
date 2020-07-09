def Check_out () :
    def Look_up () :
        test = "Have a look"
    def Watch_out () :
        nonlocal test
        test = "eyes out"
    def Take_out () :
        global test
        test = "Kill someone"

    test = "default"
    Look_up()
    print(" Look for Something "+test)
    Watch_out()
    print("Eyes off Out "+test)
    Take_out()
    print("Afraid of kill "+test)
Check_out()



