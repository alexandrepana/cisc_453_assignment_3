#!python3
import random
import agent
# ---Sarsa Agent---
# Inherits from Agent
# class. Overrides definitions
# to create Sarsa behaviour
class Sarsa(Agent):
    # Takes in a dict of action options and their values
    def select_action(self, options):
        x = random.random() # create random float between 0 - 1

        if (x > self.epsilon):
            max_value = max(options.values()) # Determine highest value option
            max_keys = [k for k, v in options.items() if v == max_value] # select they 
            return random.choice(max_keys)
        else:
            return random.choice(options.keys())

    def update_policy(self, current_state, current_action, next_state, next_action, reward):
        return