import state
import position

class GridWorld:
    def __init__(self, height, width, terminal_position, wind_columns1, wind_columns2): # terminal position is type Position, wind columns are lists of indexes with wind in them
        self.height = height
        self.width = width
        self.wc1 = wind_columns1
        self.wc2 = wind_columns2
        self.terminal = terminal_position # Designate a terminal position, or target location
        self.grid = self.generate_grid()

    def is_position_terminal(self, position):
        return (position == self.terminal)
    
    def generate_grid(self):

        temp_grid = []

        for i in range(self.height):
            
            temp = []

            for j in range(self.width):

                new_state = state.State( position.Position(i,j) ) # Initialize new state

                if(j in self.wc1): # Check if it should have wind
                    new_state.set_wind(1) # assign wind value

                elif(j in self.wc2):
                    new_state.set_wind(2) # assign wind value

                temp.append(new_state) # build row
            
            temp_grid.append(temp)
            
        return temp_grid
                
for ele in GridWorld(10, 10, position.Position(6,6), [1,3,5], [2,4,6]).grid:
    for test in ele:
        print(str(test.position.x) + " " + str(test.position.y) + " | Wind Value = " + str(test.wind))
