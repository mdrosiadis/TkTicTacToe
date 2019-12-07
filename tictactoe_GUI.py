from tkinter import *
import functools
from random import randint

def position(mylist):
    print('H thesi {} ,{}'.format(mylist[0],mylist[1]))

def changeButtonColor(btns, x, y):
    btns[x][y].config(bg = "#{:02x}{:02x}{:02x}".format(randint(0,255), randint(0,255), randint(0,255)))

def sol2(btn):
    btn.config(bg = "#{:02x}{:02x}{:02x}".format(randint(0,255), randint(0,255), randint(0,255)))

def changeStatus(btn):
    current = btn["text"]

    if current == "_":
        btn.config(text = "X")
        btn.config(state = DISABLED)

w = Tk()
w.title('TicTacToe')
w.iconbitmap('tic-tac-toe_icon.ico')
#Widget player1
e1= Entry(w, width =40 ,borderwidth = 5,fg = 'red')
e1.grid(row=0 , column = 0,columnspan =2)
e1.insert(0,'Πάιχτης 1')
#Widget player2
e2= Entry(w,width =40,borderwidth = 5,fg = 'blue')
e2.grid(row = 1,column = 0,columnspan =2)
e2.insert(1,'Πάιχτης 2')
#score widjets
Label1 = Label(w, text="Score 1",borderwidth = 5)
Label2 = Label(w, text="Score2",borderwidth = 5)
Label1.grid(row = 0,column = 2)
Label2.grid(row = 1,column = 2)

#9 buttons for the game

#I I am passing the position and button name so i can switch it with another widget


#create Buttons
startRow = 2
startCol = 0

gameSize = 3

buttons = []


for c in range(3):
    buttons.append([])
    for r in range(3):
        btn = Button(w, text = "_", padx = 50, pady= 50, fg = "red")
        btn.config(command = functools.partial(changeStatus, btn))
        btn.grid(row = startRow + r, column = startCol + c)
        buttons[-1].append(btn)


    
#Reset - Exit buttons
ResetButton = Button(w,text = "Reset",padx ='40',pady ='20',borderwidth = 2).grid(row = 5,column = 0)
Label3 = Label(w, text="Player Turn-Victory",borderwidth = 5).grid(row = 5,column = 1)
ExitButton = Button(w,text = "Exit",padx ='40',pady ='20',borderwidth = 2,command = w.quit ,).grid(row = 5,column = 2)


w.mainloop()

