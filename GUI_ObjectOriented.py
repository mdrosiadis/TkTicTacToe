from tkinter import *
import functools
from random import randint


def changeStatus(btn):
    current = btn["text"]

    if current == "_":
        btn.config(text = "X")
        btn.config(state = DISABLED)



class MyWin(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        

class MyWin2:

    def __init__(self):
        self.root = Tk()
        self.root.title('TicTacToe')
        #e = tk.Label(self.root, text = "hi")
        #e.pack()
        #Widget player1
        e1= Entry(self.root, width =40 ,borderwidth = 5,fg = 'red')
        e1.grid(row=0 , column = 0,columnspan =2)
        e1.insert(0,'Πάιχτης 1')
    
#Widget player2
        e2= Entry(self.root,width =40,borderwidth = 5,fg = 'blue')
        e2.grid(row = 1,column = 0,columnspan =2)
        e2.insert(1,'Πάιχτης 2')

#score widjets
        Label1 = Label(self.root, text="Score 1",borderwidth = 5)
        Label2 = Label(self.root, text="Score2",borderwidth = 5)
        Label1.grid(row = 0,column = 2)
        Label2.grid(row = 1,column = 2)

#create Buttons
        startRow = 2
        startCol = 0

        gameSize = 3

        buttons = []


        for c in range(gameSize):
            buttons.append([])
            for r in range(gameSize):
                btn = Button(self.root, text = "_", padx = 50, pady= 50, fg = "red")
                btn.config(command = functools.partial(changeStatus, btn))
                btn.grid(row = startRow + r, column = startCol + c)
                buttons[-1].append(btn)


        #Reset - Exit buttons
        ResetButton = Button(self.root,text = "Reset",padx ='40',pady ='20',borderwidth = 2).grid(row = 5,column = 0)
        Label3 = Label(self.root, text="Player Turn-Victory",borderwidth = 5).grid(row = 5,column = 1)
        ExitButton = Button(self.root,text = "Exit",padx ='40',pady ='20',borderwidth = 2,command = self.root.destroy).grid(row = 5,column = 2)
        
        self.root.mainloop()



if __name__ == "__main__":
    MyWin2()
