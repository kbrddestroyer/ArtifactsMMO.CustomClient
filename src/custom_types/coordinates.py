import math
import json


class Vector2(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Vector2):
            return False
        return self.x == other.x and self.y == other.y

    def __mul__(self, other: int):
        self.x *= other
        self.y *= other

    def distance(self, other):
        """Get a distance between two vectors"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def to_json(self) -> str:
        return json.dumps({'x': self.x, 'y': self.y})
