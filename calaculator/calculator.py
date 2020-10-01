from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


geometry("300x150")
    window.configure(bg="red")
    window.title("Calculatoxt='1', width=7, height=1, command=lambda: press(1), bg="green", fg="white")
    button1.grid(row=4, column=0, columnspan=1)
    button2 = Button(window, text="2", width=7, height=1, command=lambda: press(2), bg="green", fg="white")
    button2.grid(row=4, colu1, columnspan=1)
    buttonequal = Button(window, text='=', width=7, height=1, command=equalpress,bg="navy blue", fg="yellow")
    buttonequal.grid(row=5, column=2, columnspan=1)
    buttonsub = Button(window, text="-", width=7, height=1, command=lambda: press('-'), bg="yellow", fg="black")
    buttonsub.grid(row=5, column=3, columnspan=1)
    buttonclear = Button(window, text="C", width=7, height=1, command=clear, bg="orange", fg="black")
    buttonclear.grid(row=6, column=0, columnspan=1)
    buttonbackspase=Button(window, text="del", width=7, height=1, bg="orange", fg="black")
    buttonbackspase.grid(row=6, column=1, columnspan=1)
    window.mainloop()

