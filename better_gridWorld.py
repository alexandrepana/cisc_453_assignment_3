from actions import Actions
import random

#   ----Grid World----
# This class object is the Grid World game
# maintaining information on every grid tile
class Grid:
    def __init__(self, width, height, terminal_position, wind_columns1, wind_columns2):
        self.width = width
        self.height = height
        self.terminal = terminal_position
        self.reward = -1
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
        yes = (self.x == self.terminal[0] and self.y == self.terminal[1])
        if (yes):
            print(self.terminal[0])
            print(self.terminal[1])
            print('>>> TERMINAL REACHED!')
        return yes
    
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
        # find new cordinates according to current state and action
        new_x = self.x + action.value[0] 
        new_y = self.y + action.value[1] + random.choice([-1,0,1])  # Comment out the random.choice for deterministic

        # update y according to wind
        new_y -= self.wind_array[self.y][self.x]

        # check if x and y are in grid world still
        # if(new_x >= self.width or new_x < 0 or new_y >= self.height or new_y < 0):
        #     new_x = self.x
        #     new_y = self.y

        # Make sure new position is inside the bounds (clamp)
        if (new_x >= self.width):
            new_x = self.width - 1
        elif (new_x < 0):
            new_x = 0

        if (new_y >= self.height):
            new_y = self.height - 1
        elif (new_y < 0):
            new_y = 0


        print(f'Moving {action} from ({self.x}, {self.y}) to ({new_x}, {new_y})')

        self.x = new_x
        self.y = new_y
        
        return self.reward   # return reward


    # Bulkier String
    # def __str__(self):
    #     divider = ("----" * self.width) + "--"
    #     string = f"\n{divider}\n"

    #     for r in range(self.height):
    #         for c in range(self.width):
    #             string = f"{string} | {self.wind_array[r][c]}"
    #         string = f"{string} |\n{divider}\n"
        
    #     return string
