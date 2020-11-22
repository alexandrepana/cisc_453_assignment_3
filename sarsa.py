#!python3
import random

class Sarsa:
    def __init__(self, states, actions):
        self.epsilon = 0.3 # chance to take random
        self.actions = actions # action space
        self.policy = {} # Initialize each state at probability of 0
        for state in states:
            for action in actions:
                self.policy[state][action] = 0

    def update_policy(self, current_state, current_action, next_state, next_action, reward):
        self.policy[current_state][current_action] = None
    
    def select_action(self, state):
        return self.episilon_greedy(self.policy[state])
    
    def episilon_greedy(self, actions):
        x = random.random()

        if (x > self.epsilon):
            return max(actions)
        else:
            return random.choice(actions)
    


