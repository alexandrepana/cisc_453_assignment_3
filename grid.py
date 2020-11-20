#!python3

class Grid:
    def __init__(self, width, height, start_state, terminal_state):
        self.width = width
        self.height = height
        self.grid = [[0 for j in range(width)] for i in range(height)]

        self.start_state = State(random.randrange(0, width), random.randrange(1, height))
        self.terminal_state = terminal_state
        self.current_state = start_state
        self.at_terminal = False

        self.actions = ['up', 'down', 'left', 'right']
        self.current_state = None

    def check_terminal(self):
        if (self.current_state == self.terminal_state):
            return True
        return False
    
    def update_state(self, next_state):
        self.current_state = next_state
    
    def update_action(self, next_action):
        self.current_action = next_action
    
    def execute_action(self, action):
        if (action == 'up'):
            # First check if we're at top border
            self.current_state = State(self.current_state.x, self.current_state.y+1)
        elif (action == 'down'):
            # First check if we're at bottom border
            self.current_state = State(self.current_state.x, self.current_state.y-1)
        elif (action == 'right'):
            # First check if we're at right border
            self.current_state = State(self.current_state.x+1, self.current_state.y)
        elif (action == 'left'):
            # First check if we're at left border
            self.current_state = State(self.current_state.x-1, self.current_state.y)
        else:
            print(f'!!! ERROR !!!: Invalid action: {action}')
        




    
class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y


        