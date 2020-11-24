#!python3
from actions import Actions
import random
import operator

class Q_Learner:
    def __init__(self, grid, actions, epsilon, learning_rate, discount):
        self.epsilon = epsilon # chance to take random
        self.learning_rate = learning_rate
        self.discount = discount
        self.actions = actions # action space
        self.policy = [[{} for x in range(grid.width)] for y in range(grid.height)]

        # Initialize each state at probability of 0
        for r in range(grid.height):
            for c in range(grid.width):
                for action in actions:
                    self.policy[r][c][action] = 0
    
    def update_policy(self, current_state, current_action, next_state, reward):
        # print(f'Current State: {current_state}')
        # print(f'Current Action: {current_action}')
        # print(f'Next State: {next_state}')



        best_next_action = max(self.policy[next_state[0]][next_state[1]].items(), key=operator.itemgetter(1))[0]
        # print(f'Best Next Action: {best_next_action}')

        target = reward + self.discount * self.policy[next_state[0]][next_state[1]][best_next_action]
        delta = target - self.policy[next_state[0]][next_state[1]][best_next_action] - self.policy[current_state[0]][current_state[1]][current_action]
        self.policy[current_state[0]][current_state[1]][current_action] += self.learning_rate * delta

        # print(f'Changed {temp} to {self.policy[current_state[0]][current_state[1]][current_action]}')
        # self.policy[current_state[0]][current_state[1]][current_action] += self.learning_rate * (reward + self.discount * self.policy[next_state[0]][next_state[1]][best_next_action] - self.policy[current_state[0]][current_state[1]][current_action])

    
    def select_action(self, grid):
        return self.episilon_greedy(self.policy[grid.y][grid.x])
    
    def episilon_greedy(self, actions):
        x = random.random()
        
        if (x > self.epsilon):
            return max(actions.items(), key=operator.itemgetter(1))[0]
        else:
            return random.choice(list(actions.keys()))
    
    def print_policy(self):
        a_str = {
            Actions.n : 'N',
            Actions.s : 'S',
            Actions.e : 'E',
            Actions.w : 'W',
            Actions.ne : 'NE',
            Actions.nw : 'NW',
            Actions.se : 'SE',
            Actions.sw : 'SW',
        }

        string = f"\n"
        for r in range(len(self.policy)):
            for c in range(len(self.policy[r])):
                for action in self.actions:
                    string = f"{string}{a_str[action]}:{self.policy[r][c][action]:.1f} "
                string = f"{string}|"
            string = f"{string}\n"
        
        print(string)
                    
    
