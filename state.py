class State:
    def __init__(self, position):
        self.position = position
        self.wind = 0
    
    def set_wind(self, value):
        self.wind = value