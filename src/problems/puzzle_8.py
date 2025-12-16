class EightPuzzle:
    def __init__(self , initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def is_goal(self,state):
        """ Checking if the current state matches the goal """
        return state == self.goal_state
    
    def get_successors(self,state):
        """ Generate all valid moves"""
        successors = []
        zero_index = state.index(0)
        #convert index to (row , col)
        row , col = divmod(zero_index , 3)
        # possible moves 
        moves = [
                    ("up" , -1 , 0),
                    ("down" , 1 , 0),
                    ("left" , 0 , -1),
                    ("right" , 0 , 1)
                ]
        for action , dr , dc in moves:
            new_row , new_col = row + dr , col + dc
            # check if move is within the grid 
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                # creating new state by swapping 0 with target number
                state_list = list(state)
                state_list[zero_index] , state_list[new_index] = state_list[new_index] , state_list[zero_index]
                new_state = tuple(state_list) 
                # tuple to be immutable

                successors.append((action , new_state , 1))
                
        return successors