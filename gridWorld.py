import random
import actions
from actions import Actions
#   ----Grid World----
# This class object is the Grid World game
# maintaining information on every grid tile

class GridWorld:
    def __init__(self, height, width, terminal_position, wind_columns1, wind_columns2):
        self.height = height
        self.width = width
        self.wc1 = wind_columns1 # wind columns are lists of [][indexes] with wind in them
        self.wc2 = wind_columns2 # columns are either valued at 1 or 2
        self.terminal = terminal_position # Designate a terminal position # terminal position is type Position,
        self.grid = self.generate_grid() # Each grid cell contains a value

    # used to by agents to check if a terminal state has been reached
    def is_position_terminal(self, position):
        return (position == self.terminal)
    
    def find_spawn(self):
        spawn = [random.randint(0, self.height-1), random.randint(0, self.width-1)]
        if(self.is_position_terminal(spawn)): return self.find_spawn() # recursively search for a non terminal spawn position
        return(spawn)

    # grid world generator. This definition handles state creation, position assignment, and wind value assignment
    def generate_grid(self):

        temp_grid = [] # temp list to be filled and returned as grid

        for i in range(self.height): # Iterate over height of grid world
            
            temp_row = []

            for j in range(self.width): # Iterate over width of grid world

                temp_dict = {} 

                for action in Actions:
                    
                    temp_dict[action] = 0 # generate state action values

                temp_row.append(temp_dict) # build list of dictionaries

            temp_grid.append(temp_row) # build row with list of dictionaries
            
        return temp_grid

    def move(self, state, action):
        
        x = state[1]
        y = state[0]

        # update y according to wind
        if(x in self.wc1):
            y -= 1
        elif(x in self.wc2):
            y -= 2

        # find new cordinates according to current state and action
        x = x + list(action.value)[0] 
        y = y + list(action.value)[1] + random.choice([-1,0,1]) 

        # check if x and y are in grid world still
        if(y >= self.width or y < 0 or x >= self.height or x < 0):
            return state # we don't move

        return [x, y]

# --- Deprecated --- #
# Utility function used to stop wind from moving agent off the grid
def clamp(value, max_value, min_value):
        
    if( value > max_value):
        value = max_value
    elif( value < min_value):
        value = min_value
            
    return value
