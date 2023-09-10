from tkinter import *
# This is to create a basic window
win = Tk() 

# this is for the size of the window 
win.geometry("600x500")  

# this is to prevent from resizing the window
win.resizable(0, 0)  
win.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

def bt_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
 
expression = ""
 
input_text = StringVar()
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="purple", highlightcolor="black", highlightthickness=6)
 
input_frame.pack(side=TOP)
 
input_field = Entry(input_frame, font=('arial', 25, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=15) 
 
btns_frame = Frame(win, width=500, height=280, bg="purple",highlightthickness=6)
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "C",font='10', fg = "Red", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 4, pady = 4 )
 
divide = Button(btns_frame, text = "/",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 4, pady = 4)
 
# second row
 
seven = Button(btns_frame, text = "7",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 4, pady = 4)
 
eight = Button(btns_frame, text = "8",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 4, pady = 4)
 
nine = Button(btns_frame, text = "9",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 4, pady = 4)
 
multiply = Button(btns_frame, text = "*",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 4, pady = 4)
 
# third row
 
four = Button(btns_frame, text = "4",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 4, pady = 4)
 
five = Button(btns_frame, text = "5",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
  
zero = Button(btns_frame, text = "0",font='10', fg = "Red", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".",font='20', fg = "Red", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 4, pady = 4)
 
equals = Button(btns_frame, text = "=",font='10', fg = "Red", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 4, pady = 4)
 
win.mainloop()
