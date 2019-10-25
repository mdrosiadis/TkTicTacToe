class Gameboard:
    '''A gameboard for TicTacToe'''
    def __init__( self,player_names,bdata,turn,score,):
        sef.player_names=name
        sef.bdata = b.data
        self.turn= turn
        self.score = [0,0]


def victory(bdata,turn):
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

def setpos(bdata,turn):
    while True:
        pos = input ("Position")
        if str(self.bdata[pos]) is True:
            print ("Position already selected")
        else:
            bdata[pos] = turn
    return bdata

def erase_board(bdata):
    for i range (3):
        for j range(3):
            bdata[i][j] = j
return bdata




            

            
        
    
