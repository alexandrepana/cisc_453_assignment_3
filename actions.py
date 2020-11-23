from enum import Enum
north = -1
east = 1
west = -1
south = 1

class Actions(Enum):
    n   = [0, north]
    e   = [east, 0]
    s   = [0, south]
    w   = [west, 0]
    ne  = [east, north]
    nw  = [west, north]
    se  = [east, south]
    sw  = [west, south]


class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UPRIGHT = 5
    UPLEFT = 6
    DOWNRIGHT = 7
    DOWNLEFT = 8
