class Gameboard:
    '''A gameboard for TicTacToe'''
    def __init__( self,name,bdata,score):
        sef.name=name
        sef.bdata = bdata
        self.score = [0,0]


    def victory(self,symbol):
        victory = False
        a1=[[0][0],[0][1],[0][2]]
        a2=[[1][0],[1][1],[1][2]]
        a3=[[2][0],[2][1],[2][2]] 
        a4=[[0][0],[1][0],[2][0]]
        a5=[[0][1],[1][1],[2][1]]
        a6=[[0][2],[1][2],[2][2]]  
        a7=[[0][0],[1][1],[2][2]]
        a8=[[0][2],[1][1],[2][0]]
        a=[a1,a2,a3,a4,a5,a6,a7,a8]
        if [turn,turn,turn] in a:
            victory = True
        return victory

    def setpos(self,symbol):
        while True:
            pos = input ("Position")
            if str(self.bdata[pos]) is True:
                print ("Position already selected")
            else:
                self.bdata[pos] = symbol
                break
        return self.bdata

   

    def display(self):
        for i in range (3):
            for j in range(3):
                print(self.bdata[i][j],end = ' ')

 def erase_board():
     a = []
     for i in range (3):
         for j in range(3):
             a[i][j] = j
    return a
            

#Initiation script containing script to be removed from testing
a=input("Δώσε όνομα του παίχτη 1")
b = input ("Δώσε όνομα του παίχτη 2")
board = erase_board()
game = Gameboard([a,b='Computer'],board,[0,0])
while True:
    game.display()
    game.setpos('O')
    game.victory('O')
    if victory is True:
        print(f'Ο {} νίκησε'.format(game.player_name[0]))
        game.score[0]+=1
        break
    game.display()
    game.setpos('X')
    game.victory('X')
    if victory is True:
        print(f'Ο {} νίκησε'.format(game.player_name[1]))
        game.score[1]+=1
        break
    


            

            
        
    
