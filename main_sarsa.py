#!python3
from gridWorld import GridWorld
from sarsa import Sarsa
from qLearning import Q_learning
from agent import Agent
from actions import Actions

# Grid World properties
height = 7
width = 10
terminal_position = [8-1, 4-1] # indexing starts at 0 so -1
windy_columns_1   = [4-1, 5-1, 6-1, 9-1]
windy_columns_2   = [8-1,7-1]

# Agent properties
epsilon = 0.9 # Chance of making random decision
rate = 0.001
gamma = 0.85
# Agent Training properties
episodes = 1000
steps = 500


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
    reward = 0
    world = make_world()
    agent = make_agent(world.grid, agent_type)

    for episode in range(episodes):

        # Initialize episode spawn and initial action
        move_count = 0 # reset move counter
        state_1 = world.find_spawn()
        action_1 = agent.select_action(state_1)

        #print(agent.policy)

        while move_count < steps:

            #print("action one = " + str(action_1))
            # Get the next state
            state_2 = world.move(state_1, action_1)
            
            # choose next action
            action_2 = agent.select_action(state_2)

            #print("action two = " + str(action_2))

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
        
        print(move_count)

    return agent

trained_agent = train("sarsa")
trained_agent.output_policy()