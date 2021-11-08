# Show the symbols on the status bar
# Need to handle more than one operation a time
# add, minus, multiply, divide, paranthesis
from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log

window = Tk()
expression = ""
inputText = StringVar()

#function
def clickButton(item):
    global expression 
    inputText.set(inputText.get()+ (str(item)))

def clearButton():
    global expression
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)

#input frame




e = Entry(window, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)




#e.grid(row=0, column=0)
#e.pack(ipady=13)

button_1 = Button(window, text = '1', padx = 40, pady = 20, command = lambda: clickButton(1).grid(row=3, column=0))
button_2 = Button(window, text = '2', padx = 40, pady = 20, command = lambda: clickButton(2).grid(row=3, column=1))
button_3 = Button(window, text = '3', padx = 40, pady = 20, command = lambda: clickButton(3).grid(row=3, column=2))
button_4 = Button(window, text = '4', padx = 40, pady = 20, command = lambda: clickButton(4).grid(row=2, column=0))
button_5 = Button(window, text = '5', padx = 40, pady = 20, command = lambda: clickButton(5).grid(row=2, column=1))
button_6 = Button(window, text = '6', padx = 40, pady = 20, command = lambda: clickButton(6).grid(row=2, column=2))
button_7 = Button(window, text = '7', padx = 40, pady = 20, command = lambda: clickButton(7).grid(row=1, column=0))
button_8 = Button(window, text = '8', padx = 40, pady = 20, command = lambda: clickButton(8).grid(row=1, column=1))
button_9 = Button(window, text = '9', padx = 40, pady = 20, command = lambda: clickButton(9).grid(row=1, column=2))
button_0 = Button(window, text = '0', padx = 40, pady = 20, command = lambda: clickButton(0).grid(row=4, column=0))


button_equal = Button(window, text = '=', padx = 91, pady = 20, command = lambda: equalButton().grid(row=5, column=1, columnspan=2))
button_clear = Button(window, text = 'Clear', padx = 79, pady = 20, command = lambda: clearButton().grid(row=4, column=1, columnspan=2))  
button_add = Button(window, text = '+', padx = 39, pady = 20, command = lambda: clickButton('+').grid(row=5, column=0))
button_subtract = Button(window, text = '-', padx = 41, pady = 20, command = lambda: clickButton('-').grid(row=6, column=0))
button_multiply = Button(window, text = '*', padx = 40, pady = 20, command = lambda:clickButton('*').grid(row=6, column=1))
button_divide = Button(window, text = '/', padx = 40, pady = 20, command = lambda:clickButton('/').grid(row=6, column=2))



window.mainloop()



#Credit https://github.com/dineshyadav3169/advance-calculator-with-UI-in-python/blob/master/Calculator_ui.py