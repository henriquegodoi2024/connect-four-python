

import random  
from checker3 import *

class AIPlayer(Player):
    """ Artificial intelligence (AI) to choose its next move
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        self.list_score = [50]*7
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) +')'
    

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the 
            board, and that returns the index of the column with the maximum 
            score. If one or more columns are tied for the maximum score, the 
            method should apply the called AIPlayer‘s tiebreaking strategy to 
            break the tie
        """
        indices_list = []
        for x in range(len(scores)):
            if scores[x] == max(scores):
                indices_list += [x]
        
        if self.tiebreak == 'LEFT':
            return indices_list[0]
        elif self.tiebreak == 'RIGHT':
            return indices_list[-1]
        else:
            return random.choice(indices_list)
        
    def scores_for(self, b):
        """ return a list containing one score for each column
        """
        for x in range(b.width):
            if b.can_add_to(x) == False:
                self.list_score[x] = -1
            elif b.is_win_for(self.checker):
                self.list_score[x] = 100
            elif b.is_win_for(self.opponent_checker()):
                self.list_score[x] = 0
            elif self.lookahead == 0:
                return self.list_score
            else:
                p = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                b.add_checker(self.checker, x)
                
                p.scores_for(b)
                
                if p.list_score[p.max_score_column(p.list_score)] == 50:
                    self.list_score[x] = 50
                elif p.list_score[p.max_score_column(p.list_score)] == 100: 
                    self.list_score[x] = 0
                elif p.list_score[p.max_score_column(p.list_score)] == 0:
                    self.list_score[x] = 100
                
                b.remove_checker(x)
        return self.list_score
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        next_move = self.max_score_column(self.scores_for(b))
        self.num_moves += 1
        
        return next_move
                
                
                
                
                
                
        
        