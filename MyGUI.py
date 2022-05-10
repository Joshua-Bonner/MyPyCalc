from tkinter import *
import MyCalculator


def Clear_Click():
    MyGUI.entry.delete(0, END)


def Num_Click(num):
    if MyGUI.entry.get() != NONE:
        current = MyGUI.entry.get()
    if num == "." and "." in current:
        return
    MyGUI.entry.delete(0, END)
    MyGUI.entry.insert(0, str(current) + str(num))


def Operation(operator):
    MyCalculator.x = float(MyGUI.entry.get())
    MyCalculator.operation = operator
    MyGUI.entry.delete(0, END)


def Equals_Click():
    if MyCalculator.operation is None:
        return
    operator = MyCalculator.operation
    MyCalculator.y = float(MyGUI.entry.get())
    MyGUI.entry.delete(0, END)
    if operator == "+":
        MyGUI.entry.insert(0, MyCalculator.add(MyCalculator.x, MyCalculator.y))
    elif operator == "-":
        MyGUI.entry.insert(0, MyCalculator.sub(MyCalculator.x, MyCalculator.y))
    elif operator == "*":
        MyGUI.entry.insert(0, MyCalculator.mult(MyCalculator.x, MyCalculator.y))
    elif operator == "/":
        if MyCalculator.y != 0:
            MyGUI.entry.insert(0, MyCalculator.div(MyCalculator.x, MyCalculator.y))
        else:
            print("Cannot Divide by Zero!!!")
    elif operator == "^":
        MyGUI.entry.insert(0, MyCalculator.pow(MyCalculator.x, MyCalculator.y))
    else:
        print("Calculation Error!!!")


class MyGUI:
    root = Tk()
    root.title("QuackuLator")
    entry = Entry(root, width=80, relief='sunken', borderwidth=3, justify='right')
    button_equals = Button(root, text='=', padx=185, pady=20, command=Equals_Click)

    # Row 1
    button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: Num_Click(7))
    button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: Num_Click(8))
    button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: Num_Click(9))
    button_plus = Button(root, text='+', padx=38, pady=20, command=lambda: Operation("+"))
    button_power = Button(root, text='^', padx=40, pady=20, command=lambda: Operation("^"))

    # Row 2
    button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: Num_Click(4))
    button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: Num_Click(5))
    button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: Num_Click(6))
    button_minus = Button(root, text='-', padx=39, pady=20, command=lambda: Operation("-"))

    # Row 3
    button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: Num_Click(1))
    button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: Num_Click(2))
    button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: Num_Click(3))
    button_multiply = Button(root, text='*', padx=39, pady=20, command=lambda: Operation("*"))

    # Row 4
    button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: Num_Click(0))
    button_decimal = Button(root, text='.', padx=41, pady=20, command=lambda: Num_Click("."))
    button_clear = Button(root, text='C', padx=39, pady=20, command=lambda: Clear_Click())
    button_divide = Button(root, text='/', padx=39, pady=20, command=lambda: Operation("/"))

    def __init__(self):
        print("Calculator GUI Initialized!!!")
        MyGUI.entry.grid(row=0, column=0, columnspan=6)
        MyGUI.button_1.grid(row=3, column=0, padx=2, pady=2)
        MyGUI.button_2.grid(row=3, column=1)
        MyGUI.button_3.grid(row=3, column=2)
        MyGUI.button_4.grid(row=2, column=0)
        MyGUI.button_5.grid(row=2, column=1)
        MyGUI.button_6.grid(row=2, column=2)
        MyGUI.button_7.grid(row=1, column=0)
        MyGUI.button_8.grid(row=1, column=1)
        MyGUI.button_9.grid(row=1, column=2)
        MyGUI.button_0.grid(row=4, column=0)
        MyGUI.button_decimal.grid(row=4, column=1)
        MyGUI.button_clear.grid(row=4, column=2)
        MyGUI.button_equals.grid(row=5, column=0, columnspan=5)
        MyGUI.button_plus.grid(row=1, column=4)
        MyGUI.button_minus.grid(row=2, column=4)
        MyGUI.button_multiply.grid(row=3, column=4)
        MyGUI.button_divide.grid(row=4, column=4)
        MyGUI.button_power.grid(row=1, column=5)
        MyGUI.root.mainloop()
