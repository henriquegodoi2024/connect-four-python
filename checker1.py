

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, init_height, init_width):
        ''' constructor method for the Board Class that takes 
        height, width and slows as attibutes'''
        self.height = init_height
        self.width = init_width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
            
        s += '-' * (2 * self.width + 1) 
        s += '\n'
        
        for i in range(self.width):
            s += ' ' + str(i % 10)
            
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
            
        self.slots[row - 1][col] = checker

    
    ### add your reset method here ###
    
    def reset(self):
        '''resets the board object''' 
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def can_add_to(self, col):
        '''retuns True if there are available spaces to add checker
        is a certain column and false otherwise'''
        if 0 <= col < self.width and self.slots[0][col] == ' ':
            return True
        
        else:
            return False
        
    def is_full(self): 
        '''return True if the board is full, False otherwise.'''
        for col in range(self.width):
            
            if self.can_add_to(col):  
                
                return False     
            
        return True   

    def remove_checker(self, col):
        '''remove the top checker from column col, if there is one.'''
        assert 0 <= col < self.width
    
        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
    
        if row < self.height:
            self.slots[row][col] = ' '
            
    def is_horizontal_win(self, checker):
        """checks for a horizontal win for the specified checker."""
        for row in range(self.height):
            for col in range(self.width - 3):
                
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        
        return False


    def is_vertical_win(self, checker):
        """checks for a vertical win for the specified checker."""
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        return False


    def is_down_diagonal_win(self, checker):
        """checks for a down-right diagonal win for checker."""
        
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        return False


    def is_up_diagonal_win(self, checker):
        """checks for an up-right diagonal win for checker."""
        
        for row in range(3, self.height):
            for col in ra3nge(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        return False


    def is_win_for(self, checker):
        """returns True if there is a win for checker ('X' or 'O')."""
        assert(checker == 'X' or checker == 'O')

        return self.is_horizontal_win(checker) or \
               self.is_vertical_win(checker) or \
               self.is_down_diagonal_win(checker) or \
               self.is_up_diagonal_win(checker)

