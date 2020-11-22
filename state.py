class State:
    def __init__(self, position):
        self.position = position # Position is a vector2 point
        self.wind = 0 # Wind effect on this grid state
    
    def set_wind(self, value): # Called to set a wind value to a grid state
        self.wind = value