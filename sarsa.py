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
    def select_action(self, state):

        x = random.random() # create random float between 0 - 1

        if (x > self.epsilon):
            max_value = max(self.policy[state[0]][state[1]].values) # determine the highest value
            max_keys = [k for k, v in self.policy.items() if v == max_value] # determine their keys
            return random.choice(list(max_keys)) # return an action with the highest value
        else:
            return random.choice(list(Actions)) # return a random action

    def update_policy(self, state, action, next_state, next_action, reward):
        expected = self.policy[state[0],state[1]][action]
        actual = reward + self.gamma * self.policy[next_action[0], next_action[1]][next_action]
        self.policy[state[0], state[1]][action] += self.rate * (actual - expected)
        

    def output_policy(self): # print utility
        for row in self.policy:
            row = []
            for cell in row:
                row.append(cell.value)
            print(row)

