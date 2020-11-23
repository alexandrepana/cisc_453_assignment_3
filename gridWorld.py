import random
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
        spawn = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
        if(self.is_position_terminal(spawn)): return find_spawn() # recursively search for a non terminal spawn position
        return(spawn)

    # grid world generator. This definition handles state creation, position assignment, and wind value assignment
    def generate_grid(self):

        temp_grid = [] # temp list to be filled and returned as grid

        for i in range(self.height): # Iterate over height of grid world
            
            temp = []

            for j in range(self.width): # Iterate over width of grid world

                temp.append(0) # build row
            
            temp_grid.append(temp)
            
        return temp_grid
