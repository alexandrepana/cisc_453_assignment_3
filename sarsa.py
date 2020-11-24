#!python3
import operator
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
        #print(state)
        if (x > self.epsilon):
            max_value = max(self.policy[state[0]][state[1]], key=self.policy[state[0]][state[1]].get) # determine the highest value key
            # print("greedy action")
            return max_value # return an action with the highest value
        else:
            # print("Random action")
            return random.choice(list(self.policy[state[0]][state[1]].keys())) # return a random action

    def update_policy(self, state, action, next_state, next_action, reward):
        expected = self.policy[state[0]][state[1]][action]
        actual = reward + self.gamma * self.policy[next_state[0]][next_state[1]][next_action]
        self.policy[state[0]][state[1]][action] = self.policy[state[0]][state[1]][action] + self.rate * (actual - expected)
        

    def output_policy(self): # print utility
        for row in self.policy:
            row = []
            for cell in row:
                row.append(cell.value)
                if(cell.value == 0):
                    print("There is a 0 key")
            #print(row)

