class Gameboard:
    '''A gameboard for TicTacToe'''
    def __init__( self,name,bdata,score):
        self.name=name
        self.bdata = bdata
        self.score = [0,0]


    def victory(self,symbol):
        victory = False
        s1=self.bdata[0][0]
        s2=self.bdata[0][1]
        s3=self.bdata[0][2]
        s4=self.bdata[1][0]
        s5=self.bdata[1][1]
        s6=self.bdata[1][2]
        s7=self.bdata[2][0]
        s8=self.bdata[2][1]
        s9=self.bdata[2][2]

        a=[[s1,s2,s3],[s4,s5,s6],[s7,s8,s9],[s1,s4,s7],[s2,s5,s8],[s3,s6,s9],[s1,s5,s9],[s3,s5,s7]]
        if [symbol,symbol,symbol] in a:
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
                print(self.bdata[i][0],self.bdata[i][1],self.bdata[i][2],sep = '\t')

def erase_board():
    a = [1,2,3],[4,5,6],[7,8,9]
    return a
            

#Initiation script containing script to be removed from testing
a=input("Δώσε όνομα του παίχτη 1")
b = input ("Δώσε όνομα του παίχτη 2")
board = erase_board()
game = Gameboard([a,b],board,[0,0])
while True:
    game.display()
    game.setpos('O')
    victory = game.victory('O')
    if victory is True:
        print('Ο {} νίκησε'.format(game.player_name[0]))
        game.score[0]+=1
        break
    game.display()
    game.setpos('X')
    victory=game.victory('X')
    if victory is True:
        print('Ο {} νίκησε'.format(game.player_name[1]))
        game.score[1]+=1
        break
    


            

            
        
    
