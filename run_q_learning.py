#!python3
from actions import Actions
import better_gridWorld
import q_learning


# ALEX'S CODE
#####################

def train_q_learning(grid, episodes, max_steps, actions, epsilon, learning_rate, discount):
    q_learner = q_learning.Q_Learner(grid, actions, epsilon, learning_rate, discount)
    print(grid)

    # Loop for each episode
    for episode in range(episodes):
        step = 1

        # Initialize state
        grid.randomize_position()
        # action = q_learner.select_action(grid)

        reward2 = 0
        # Loop for each step of episode
        while (not grid.at_terminal()):

            # Choose A from S using policy derived from Q
            action = q_learner.select_action(grid)

            # Execute action
            prev_x = grid.x
            prev_y = grid.y
            reward = grid.move(action)
            reward2 -= 1

            q_learner.update_policy([prev_y, prev_x], action, [grid.y, grid.x], reward)

            # q_learner.print_policy()

            # input("Press Enter to continue...")

            step += 1
            if (step > max_steps):
                print('>>> Max Steps reached.')
                break
        print(f'Steps until completion: {step}')
        # input("Press Enter to continue...")



def __main__():
    # Define training variables
    episodes = 1000
    max_steps = 10000
    epsilon = 0.05
    learning_rate = 0.001
    discount = 0.85
    cardinal_moves = [Actions.n, Actions.e, Actions.s, Actions.w]
    kings_moves = [Actions.n, Actions.e, Actions.s, Actions.w, Actions.ne, Actions.nw, Actions.se, Actions.sw]

    # Define our Grid
    width = 10
    height = 7
    wind_columns1 = [3, 4, 5, 8]
    wind_columns2 = [6, 7]
    terminal_position = (7, 4)
    grid = better_gridWorld.Grid(width, height, terminal_position, wind_columns1, wind_columns2)

    # Start Training
    train_q_learning(grid, episodes, max_steps, cardinal_moves, epsilon, learning_rate, discount)
    train_q_learning(grid, episodes, max_steps, kings_moves, epsilon, learning_rate, discount)


    
        
__main__()
