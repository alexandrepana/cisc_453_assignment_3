from actions import Action
import random
#   ----Grid World----
# This class object is the Grid World game
# maintaining information on every grid tile
class Grid:
    def __init__(self, width, height, terminal_position, wind_columns1, wind_columns2):
        self.width = width
        self.height = height
        self.terminal = terminal_position
        self.generate_wind_array(wind_columns1, wind_columns2)
        self.randomize_position()
    
    # Create 2D array of wind at each position
    def generate_wind_array(self, wc1, wc2):
        self.wind_array = [[0 for x in range(self.width)] for y in range(self.height)]

        for r in range(self.height):
            for c in range(self.width):
                wind = 0
                if (c in wc1):
                    wind = 1
                elif (c in wc2):
                    wind = 2
                
                self.wind_array[r][c] = wind
                

    # Returns true if given position is terminal
    def at_terminal(self):
        return (self.x == self.terminal[0] and self.y == self.terminal[1])
    
    # Returns a random coordinate on the grid
    def randomize_position(self):
        self.x = random.randrange(0, self.width)
        self.y = random.randrange(0, self.height)
    
    # Lets us print the grid in a nice format
    def __str__(self):
        string = f"\n"

        for r in range(self.height):
            for c in range(self.width):
                string = f"{string} {self.wind_array[r][c]}"
            string = f"{string}\n"
        
        return string
    
    def move(self, action):
        # Cardinal Moves
        if (action == Action.UP):
            self.y += 1
        elif (action == Action.DOWN):
            self.y -= 1
        elif (action == Action.LEFT):
            self.x -= 1
        elif (action == Action.RIGHT):
            self.x += 1
        
        # Kings Moves
        elif (action == Action.UPRIGHT):
            self.y += 1
            self.x += 1
        elif (action == Action.UPLEFT):
            self.y += 1
            self.x -= 1
        elif (action == Action.DOWNRIGHT):
            self.y -= 1
            self.x += 1
        elif (action == Action.DOWNLEFT):
            self.y -= 1
            self.x -= 1


    # Bulkier String
    # def __str__(self):
    #     divider = ("----" * self.width) + "--"
    #     string = f"\n{divider}\n"

    #     for r in range(self.height):
    #         for c in range(self.width):
    #             string = f"{string} | {self.wind_array[r][c]}"
    #         string = f"{string} |\n{divider}\n"
        
    #     return string
