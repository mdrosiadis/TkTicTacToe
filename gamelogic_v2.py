class Gameboard:
    '''A gameboard for TicTacToe'''
    

    def __init__(self, size, names):
        self.names = {'X' : names[0], 'O' : names[1]}
        self.size = size
      
        
        self.bdata = [[" " for __ in range(self.size)] for _ in range(self.size)]
        
        '''
        self.data[x][y] 
           x->
            0   1   2
        y 0   |   | 
        |  ---+---+---
        V 1   |   |   
           ---+---+---
          2   |   |   
       
        '''
        
        
        #self.score = [0,0]
        
        self.scores = {'X' : 0, 'O' : 0}
        self.activeS = 'X'
        
        # more to come


    def victory(self, symbol = None):
        """
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
        """
        if symbol is None:
            symbol = self.activeS

    
        # vertical lines:
        for x in range(self.size):
            for y in range(self.size):
              if self.bdata[x][y] != symbol:
                break
            else:
              return True
        
        # horizontal lines:
        for y in range(self.size):
            for x in range(self.size):
              if self.bdata[x][y] != symbol:
                break
            else:
              return True
            
        # diagonal lines:
        pd, sd = 0, 0
        for i in range(self.size):
          if self.bdata[i][i] == symbol:
            pd += 1
          if self.bdata[i][self.size - i - 1] == symbol: # bsize - i - 1
            sd += 1
        
        return pd == self.size or sd == self.size
                
              
        

    def setpos(self, pos, symbol = None):
        # pos -> tuple (int , int) 0-2 as for x , y
        """
        while True:
            pos = input ("Position")
            if str(self.bdata[pos]) is True:
                print ("Position already selected")
            else:
                self.bdata[pos] = symbol
                break
        return self.bdata
        """
        if symbol is None:
            symbol = self.activeS
        
        if self.bdata[pos[0]][pos[1]] == " ":
            self.bdata[pos[0]][pos[1]] = symbol
        else:
            print("Position already taken!")
        
    def reset_board(self):
        self.bdata = [[" " for __ in range(self.size)] for _ in range(self.size)]
    
    def display(self):
        print(f"Player {self.names[self.activeS]}({self.activeS}) is playing:\n")
        for y in range (self.size):
            for x in range(self.size):
                print(f" {self.bdata[x][y]} ", end = "")
                if x < self.size - 1:
                    print("|", end = "")
            print()
            if y < self.size - 1:
                print("---+---+---")
            
        print()
        print(f"Score: {self.names['X']} : {self.scores['X']} - {self.names['O']} : {self.scores['O']}")
        
    def next_player(self):
      self.activeS = 'X' if self.activeS == 'O' else 'O'

"""
def erase_board():
    a = [1,2,3],[4,5,6],[7,8,9]
    return a
"""

#Initiation script containing script to be removed from testing
a = input("Δώσε όνομα του παίχτη 1: ")
b = input("Δώσε όνομα του παίχτη 2: ")
game = Gameboard(3, (a, b))

while True:
    game.display()
    x = int(input("Give X: "))
    y = int(input("Give Y: "))
    
    game.setpos((x, y))
    
    if game.victory():
        game.display()
        print("win!")
        game.reset_board()
    else:
        game.next_player()

            
        
    
