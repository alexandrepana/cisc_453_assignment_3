#!python3
import gridWorld
import state
import position
import sarsa
import qLearning
import agent

# Grid World properties
height = 7
width = 10
terminal_position = position.Position(8-1, 4-1) # indexing starts at 0 so -1
windy_columns_1 = [4-1, 5-1, 6-1, 9-1]
windy_columns_2 = [8-1,7-1]

# Agent properties
epsilon = 0.3 # Chance of making random decision
steps = 10000
rate = 0.001
gamma = 0.85
actions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

# Initializes a Grid World
def make_world():
    return gridWorld.GridWorld(height,width, terminal_position, windy_columns_1, windy_columns_2)

# Create an agent object of given type
def make_agent(states, agent_type):
    if(agent_type == "sarsa"):
        return sarsa.Sarsa(states, actions, epsilon, rate, gamma)
    elif(agent_type == "q"):
        return agent.Agent(states, actions, epsilon, rate, gamma) # replace with q-learn
    else:
        return agent.Agent(states, actions, epsilon, rate, gamma)

def run(agent_type):
    world = make_world()
    agent = make_agent(world.grid, agent_type)