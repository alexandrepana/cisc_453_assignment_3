#!python3
from actions import Action
import gridWorld
import better_gridWorld
import position
import sarsa
import q_learning

def train_sarsa(grid, episodes):
    for episode in range(episodes):
        # Initialize State

        # Choose Initial Action from State using Policy

        while (not current_state.termial):
            pass
            # Execute Action, get Reward and State'

            # Choose Action' from State' using Policy

            # Update Policy

            # S = S', A = A'

def train_q_learning(grid, episodes, actions):
    q_learner = q_learning.Q_Learner(grid, actions)
    print(grid)
    print(f'Starting Position on Grid: ({grid.x}, {grid.y})')

    # Loop for each episode
    for episode in range(episodes):
        # Initialize state
        grid.randomize_position()

        # Loop for each step of episode
        while (not grid.at_terminal()):
            # grid.randomize_position()

            print(f'Before action: ({grid.x}, {grid.y})')

            # Choose A from S using policy derived from Q
            action = q_learner.select_action(grid)

            # Execute action
            grid.move(action)

            print(f'After {action}: ({grid.x}, {grid.y})')

            input("Press Enter to continue...")





def __main__():
    # Define training variables
    episodes = 1000
    cardinal_moves = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]
    kings_moves = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT, Action.UPRIGHT, Action.UPLEFT, Action.DOWNRIGHT, Action.DOWNLEFT]

    # Define our Grid
    width = 10
    height = 7
    wind_columns1 = [3, 4, 5, 8]
    wind_columns2 = [6, 7]
    terminal_position = (7, 4)
    grid = better_gridWorld.Grid(width, height, terminal_position, wind_columns1, wind_columns2)

    # train_sarsa(episodes)

    train_q_learning(grid, episodes, cardinal_moves)


    
        
if __name__ == '__main__':
    __main__()
