#!python3
from gridWorld import GridWorld
from sarsa import Sarsa
from agent import Agent
from actions import Actions
import better_gridWorld
import q_learning


# BRYAN'S CODE
###########################

# Grid World properties
height = 7
width = 10
terminal_position = [8-1, 4-1] # indexing starts at 0 so -1
windy_columns_1   = [4-1, 5-1, 6-1, 9-1]
windy_columns_2   = [8-1,7-1]

# Agent properties
epsilon = 0.3 # Chance of making random decision
rate = 0.001
gamma = 0.85
# Agent Training properties
episodes = 10000
steps = 100
reward = 0

# Initializes a Grid World
def make_world():
    return GridWorld(height, width, terminal_position, windy_columns_1, windy_columns_2)

# Create an agent object of given type
def make_agent(grid, agent_type):
    if(agent_type == "sarsa"):
        return Sarsa(grid, epsilon, rate, gamma)
    elif(agent_type == "q"):
        return Q_learning(grid, epsilon, rate, gamma)
    else:
        return Agent(grid, epsilon, rate, gamma)

def train(agent_type):
    world = make_world()
    agent = make_agent(world.grid, agent_type)

    for episode in range(episodes):

        # Initialize episode spawn and initial action
        move_count = 0 # reset move counter
        state_1 = world.find_spawn()
        action_1 = agent.select_action(state_1)

        while move_count < steps:

            # Get the next state
            state_2 = world.move(action_1)
            
            # choose next action
            action_2 = agent.select_action(state_2)

            # Update q value 
            agent.update_policy(state_1, action_1, state_2, action_2, reward)

            # assign new action states
            state_1 = state_2
            action_1 = action_2

            # update move count and reward 
            move_count+=1
            reward -= 1

            # check if state is terminal
            if(world.is_position_terminal(state_1)): break

    return agent

# trained_agent = train("sarsa")
# trained_agent.output_policy()

# world = make_world()
# agent = make_agent(world.grid, "sarsa")

# print(agent.select_action([0,0]))





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
        print(f'Starting Position on Grid: ({grid.x}, {grid.y})')
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

            input("Press Enter to continue...")

            step += 1
            if (step > max_steps):
                print('>>> Max Steps reached.')
                break
        print(f'Steps until completion: {step}')
        input("Press Enter to continue...")



def __main__():
    # Define training variables
    episodes = 1000
    max_steps = 10000
    cardinal_moves = [Actions.n, Actions.e, Actions.s, Actions.w]
    kings_moves = [Actions.n, Actions.e, Actions.s, Actions.w, Actions.ne, Actions.nw, Actions.se, Actions.sw]

    # Define our Grid
    width = 10
    height = 7
    wind_columns1 = [3, 4, 5, 8]
    wind_columns2 = [6, 7]
    terminal_position = (7, 4)
    grid = better_gridWorld.Grid(width, height, terminal_position, wind_columns1, wind_columns2)

    # Values
    
    epsilon = 0.05
    learning_rate = 0.001
    discount = 0.85
    train_q_learning(grid, episodes, max_steps, cardinal_moves, epsilon, learning_rate, discount)


    
        
if __name__ == '__main__':
    __main__()
