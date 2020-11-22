# --- Agent ---
# Base class for
# all agent types
class Agent:
    def __init__(self, states, actions, epsilon, learn_rate, gamma): # This may need to be thinned out and seperated into appropriate agent types overrides
        self.epsilon = epsilon  # chance to take random
        self.actions = actions  # action space
        self.rate = learn_rate  # learn rate
        self.gamma = gamma      # gamma
        self.policy = {}        # State dict initialized all at 0
    
    # Define overides 
    def select_action(self, options):
        return max(options)
    
    def update_policy(self, current_state, current_action, next_state, next_action, reward):
        return self.policy