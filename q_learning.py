#!python3
from actions import Action
import random

class Q_Learner:
    def __init__(self, grid, actions):
        self.epsilon = 0.3 # chance to take random
        self.actions = actions # action space
        self.policy = [[{} for x in range(grid.width)] for y in range(grid.height)]

        # Initialize each state at probability of 0
        for r in range(grid.height):
            for c in range(grid.width):
                for action in actions:
                    self.policy[r][c][action] = 0

    def update_policy(self, current_state, current_action, next_state, next_action, reward):
        self.policy[current_state][current_action] = None
    
    def select_action(self, state):
        return random.choices(self.actions)[0]
        # return self.episilon_greedy(self.policy[state])
    
    def episilon_greedy(self, actions):
        x = random.random()

        if (x > self.epsilon):
            return max(actions)
        else:
            return random.choice(actions)
    
