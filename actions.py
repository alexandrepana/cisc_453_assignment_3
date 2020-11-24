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