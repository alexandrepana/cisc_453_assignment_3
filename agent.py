# --- Agent ---
# Base class for
# all agent types
class Agent:
    def __init__(self, grid, epsilon, learn_rate, gamma): # This may need to be thinned out and seperated into appropriate agent types overrides
        self.epsilon = epsilon  # chance to take random
        self.rate = learn_rate  # learn rate
        self.gamma = gamma      # gamma
        self.policy = grid      # Grid world grid states as values

    # Define overides 
    def select_action(self):
        return 0
    
    def update_policy(self, current_state, current_action, next_state, next_action, reward):
        return 0