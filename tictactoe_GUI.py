
from tkinter import *

def position(mylist):
    print('H thesi {} ,{}'.format(mylist[0],mylist[1])
    




w =Tk()
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
myButton1= Button(w, text = "0,0",padx ='50',pady='50',fg = 'blue',command = lambda position([0,0],myButton1)).grid(row = 2,column = 0)



myButton2 = Button(w, text = "1,0",padx ='50',pady='50',fg = 'white').grid(row = 2,column = 1)
myButton3 = Button(w, text = "2,0",padx ='50',pady='50',fg = 'white').grid(row = 2,column = 2)
myButton4 = Button(w, text = "0,1",padx ='50',pady='50',fg = 'white').grid(row = 3,column = 0)
myButton5 = Button(w, text = "1,1",padx ='50',pady='50',fg = 'white').grid(row = 3,column = 1)
myButton6 = Button(w, text = "2,1",padx ='50',pady='50',fg = 'white').grid(row = 3,column = 2)
myButton7 = Button(w, text = "0,2",padx ='50',pady='50',fg = 'white').grid(row = 4,column = 0)
myButton8 = Button(w, text = "1,2",padx ='50',pady='50',fg = 'white').grid(row = 4,column = 1)
myButton9 = Button(w, text = "2,2",padx ='50',pady='50',fg = 'white').grid(row = 4,column = 2)

#Reset - Exit buttons

ResetButton = Button(w,text = "Reset",padx ='40',pady ='20',borderwidth = 2).grid(row = 5,column = 0)

Label3 = Label(w, text="Player Turn-Victory",borderwidth = 5).grid(row = 5,column = 1)

ExitButton = Button(w,text = "Exit",padx ='40',pady ='20',borderwidth = 2,command = w.quit ,).grid(row = 5,column = 2)


w.mainloop()

