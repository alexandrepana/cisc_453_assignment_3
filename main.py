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
epsilon = 0.3 # Chance of making random decision
rate = 0.001
gamma = 0.85
# Agent Training properties
episodes = 10000
steps = 100

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

def run(agent_type):
    world = make_world()
    agent = make_agent(world.grid, agent_type)

    for episode in range(episodes):
        attempts = 0
        state_1 = world.find_spawn()
        action1 = agent.select_action(state_1, world)


run("sarsa")
