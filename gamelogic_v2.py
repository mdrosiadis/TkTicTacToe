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
                
        self.scores = {'X' : 0, 'O' : 0}
        self.activeS = 'X'
        
        # more to come
        
    def victory(self, symbol = None):
        if symbol is None:
            symbol = self.activeS

        if self.check_lines(symbol):
            self.scores[symbol] += 1
            return True
        
        return False
    
    def check_lines(self, symbol):
        
        """
        if symbol is None:
            symbol = self.activeS
		"""
    
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

            

