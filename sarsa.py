#!python3
import random
from agent import Agent
from actions import Actions
# ---Sarsa Agent---
# Inherits from Agent
# class. Overrides definitions
# to create Sarsa behaviour
class Sarsa(Agent):
    # Takes in a dict of action options and their values
    def select_action(self, state, world):

        x = random.random() # create random float between 0 - 1
        options = self.determine_options(state, world)

        if (x > self.epsilon):
            max_value = max(options.values()) # determine the highest value
            max_keys = [k for k, v in options.items() if v == max_value] # determine their keys
            return random.choice(max_keys) # return a key with the highest value
        else:
            return random.choice(options) # return a random key

    def update_policy(self, state, action, next_state, next_action, reward):
        #expected = self.policy[]
        return 0
    
    #
    def determine_options(self, state, world):
        options = {}
        for action in Actions:
            
            newX = action.value[0] + state[0]
            newY = action.value[1] + state[1]

            if( newX < 0 | newX >= world.width | newY < 0 | newY >= world.height):
                options[action] = 0
            else:
                options[action] = self.policy[newX, newY]

        return options
            