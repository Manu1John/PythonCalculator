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



if __name__ == "__main__":
    window = Tk()
    window.geometry("300x150")
    window.configure(bg="red")
    window.title("Calculator")
    label = LabelFrame(window, text="CrossRoads", fg="black")
    label.grid(padx=10, pady=10)
    equation = StringVar()
    display = Entry(window, width="60", textvariable=equation)
    display.grid(columnspan=10, ipadx=10)
    equation.set("Enter your Expression")
    button7 = Button(window, text='7', width=7, height=1, command=lambda: press(7), bg="green", fg="white")
    button7.grid(row=2, column=0, columnspan=1)
    button8 = Button(window, text="8", width=7, height=1, command=lambda: press(8), bg="green", fg="white")
    button8.grid(row=2, column=1, columnspan=1)
    button9 = Button(window, text='9', width=7, height=1, command=lambda: press(9), bg="green", fg="white")
    button9.grid(row=2, column=2, columnspan=1)
    buttondiv = Button(window, text="/", width=7, height=1, command=lambda: press("/"), bg="yellow", fg="black")
    buttondiv.grid(row=2, column=3, columnspan=1)
    button4 = Button(window, text='4', width=7, height=1, command=lambda: press(4), bg="green", fg="white")
    button4.grid(row=3, column=0, columnspan=1)
    button5 = Button(window, text="5", width=7, height=1, command=lambda: press(5), bg="green", fg="white")
    button5.grid(row=3, column=1, columnspan=1)
    button6 = Button(window, text='6', width=7, height=1, command=lambda: press(6), bg="green", fg="white")
    button6.grid(row=3, column=2, columnspan=1)
    buttonmulti = Button(window, text="*", width=7, height=1, command=lambda: press("*"), bg="yellow", fg="black")
    buttonmulti.grid(row=3, column=3, columnspan=1)
    button1 = Button(window, text='1', width=7, height=1, command=lambda: press(1), bg="green", fg="white")
    button1.grid(row=4, column=0, columnspan=1)
    button2 = Button(window, text="2", width=7, height=1, command=lambda: press(2), bg="green", fg="white")
    button2.grid(row=4, column=1, columnspan=1)
    button3 = Button(window, text='3', width=7, height=1, command=lambda: press(3), bg="green", fg="white")
    button3.grid(row=4, column=2, columnspan=1)
    buttonplus = Button(window, text="+", width=7, height=1, command=lambda: press("+"), bg="yellow", fg="black")
    buttonplus.grid(row=4, column=3, columnspan=1)
    buttondot = Button(window, text='.', width=7, height=1, command=lambda: press('.'), bg="green", fg="white")
    buttondot.grid(row=5, column=0, columnspan=1)
    buttonzero = Button(window, text="0", width=7, height=1, command=lambda: press(0), bg="green", fg="white")
    buttonzero.grid(row=5, column=1, columnspan=1)
    buttonequal = Button(window, text='=', width=7, height=1, command=equalpress,bg="navy blue", fg="yellow")
    buttonequal.grid(row=5, column=2, columnspan=1)
    buttonsub = Button(window, text="-", width=7, height=1, command=lambda: press('-'), bg="yellow", fg="black")
    buttonsub.grid(row=5, column=3, columnspan=1)
    buttonclear = Button(window, text="C", width=7, height=1, command=clear, bg="orange", fg="black")
    buttonclear.grid(row=6, column=0, columnspan=1)
    buttonbackspase=Button(window, text="del", width=7, height=1, bg="orange", fg="black")
    buttonbackspase.grid(row=6, column=1, columnspan=1)
    window.mainloop()

