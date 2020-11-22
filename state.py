class State:
    def __init__(self, value):
        self.value = value  # how valued is this state
        self.wind = 0       # Wind effect on this grid state
    
    def set_wind(self, value):      # Called to set a wind value to a grid state
        self.wind = value
    
    def update_value(self, value):  # called to update value for being selected
        self.value = value