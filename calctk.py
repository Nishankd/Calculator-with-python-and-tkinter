from tkinter import *

# declaring the expression variable globally
expression = ''


def number_press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except Exception as ex:
        equation.set('Error')
        expression = ''


def clear():
    global expression
    expression = ''

    equation.set('')


# driver code (directly)
if __name__ == '__main__':
    # create a GUI window
    window = Tk()
    window.configure()
    window.title('Nishan Calculator')
    window.geometry('500x400')

    equation = StringVar()
    expression_field = Entry(window, textvariable=equation, width=12, font='calibre 20')
    expression_field.grid(columnspan=4, ipadx=100)
    # creating buttons
    button1 = Button(window, text='1', fg='black', bg='orange',
                     command=lambda: number_press(1), height=3, width=9)
    button1.grid(row=2, column=0)

    button2 = Button(window, text='2', fg='black', bg='orange',
                     command=lambda: number_press(2), height=3, width=9)
    button2.grid(row=2, column=1)

    button3 = Button(window, text='3', fg='black', bg='orange',
                     command=lambda: number_press(3), height=3, width=9)
    button3.grid(row=2, column=2)

    button4 = Button(window, text='4', fg='black', bg='orange',
                     command=lambda: number_press(4), height=3, width=9)
    button4.grid(row=3, column=0)

    button5 = Button(window, text='5', fg='black', bg='orange',
                     command=lambda: number_press(5), height=3, width=9)
    button5.grid(row=3, column=1)

    button6 = Button(window, text='6', fg='black', bg='orange',
                     command=lambda: number_press(6), height=3, width=9)
    button6.grid(row=3, column=2)

    button7 = Button(window, text='7', fg='black', bg='orange',
                     command=lambda: number_press(7), height=3, width=9)
    button7.grid(row=4, column=0)

    button8 = Button(window, text='8', fg='black', bg='orange',
                     command=lambda: number_press(8), height=3, width=9)
    button8.grid(row=4, column=1)

    button9 = Button(window, text='9', fg='black', bg='orange',
                     command=lambda: number_press(9), height=3, width=9)
    button9.grid(row=4, column=2)

    button0 = Button(window, text='0', fg='black', bg='orange',
                     command=lambda: number_press(0), height=3, width=9)
    button0.grid(row=5, column=0)

    plus = Button(window, text='+', fg='black', bg='orange',
                  command=lambda: number_press('+'), height=3, width=9)
    plus.grid(row=2, column=3)

    minus = Button(window, text='-', fg='black', bg='orange',
                   command=lambda: number_press('-'), height=3, width=9)
    minus.grid(row=3, column=3)

    divide = Button(window, text='/', fg='black', bg='orange',
                    command=lambda: number_press('/'), height=3, width=9)
    divide.grid(row=4, column=3)

    multiply = Button(window, text='*', fg='black', bg='orange',
                      command=lambda: number_press('*'), height=3, width=9)
    multiply.grid(row=5, column=3)

    equal = Button(window, text='=', fg='black', bg='orange',
                   command=equal_press, height=3, width=9)
    equal.grid(row=5, column=2)

    clear = Button(window, text='Clear', fg='black', bg='orange',
                   command=clear, height=3, width=9)
    clear.grid(row=5, column=1)

    decimal = Button(window, text='.', fg='black', bg='orange',
                     command=lambda: number_press('.'), height=3, width=9)
    decimal.grid(row=6, column=0)

    window.mainloop()