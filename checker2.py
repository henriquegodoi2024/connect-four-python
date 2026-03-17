

from checker1 import Board

class Player:
    '''constructs a new player object '''
    def __init__(self,checker):
        
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        ''' returns a string representation of player object'''
        
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        '''returns a string representation of one character representing
        the opponent'''
        
        if self.checker == 'O':
            return 'X'
        
        else:
            return 'O'
        
    
    def next_move(self, b):
        '''accepts a Board object b as a parameter and returns the column where the player 
        wants to make the next move'''
        
        
        next_move = int(input('Enter a column: '))
        while b.can_add_to(next_move) == False:
             print('Try again! ')
             next_move = int(input('Enter a column: '))   
        self.num_moves += 1
        return next_move