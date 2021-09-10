from tkinter import *
import tkinter.font as font 

def add():
    a = int(enter1.get()) #getting first input -->remember the entry name, in this sec entry1 is my first input
    b = int(enter2.get())
    result['text'] = a+b    # here result is a label which we have defined in the code and in that text stores result of a+b
def sub():
    a = int(enter1.get())
    b = int(enter2.get())
    result['text'] = a-b
def mul():
    a = int(enter1.get())
    b = int(enter2.get())
    result['text'] = a*b
def div():
    a = int(enter1.get())
    b = int(enter2.get())
    result['text'] = a/b

root = Tk() #defining the object for Tk () class
root.title("Sachu's Calci")
root.geometry('800x500') # this is to define the size of screen --> width X height
lab = Label(root, text="This is a simple calculator", bg="yellow", fg='blue', font=font.BOLD) #this is just to insert a text line in program
num1 = Label(root, text='Enter the first number',font=("Serif",12)) 
enter1 = Entry(root) #this is to accept the user values 
num2 = Label(root, text='Enter the second number', font=('Serif',12))
enter2 = Entry(root)

add = Button(root, text='add',width=8, command= add)   #it creates a Button  and command is calling the add() method to perform specific task
sub = Button(root, text='sub', width=8, command= sub)
mul = Button(root, text='mul', width=8, command=mul)
div = Button(root, text='div',width=8, command=div)

result = Label(root,font='Bold', width= 28) 

lab.grid(row=0) #this is to set the values on screen in specific location
num1.grid(row=1, column=0)
enter1.grid(row=1, column=1)
num2.grid(row=2, column=0)
enter2.grid(row=2, column=1)
add.grid(row=3, column=0)
sub.grid(row=3, column=1)
mul.grid(row=4, column=0)
div.grid(row=4, column=1)
result.grid(row=5)
root.mainloop() # this is the main driver program , without this the program would not show you GUI 