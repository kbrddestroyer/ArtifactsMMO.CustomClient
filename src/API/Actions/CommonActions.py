from src.API.ArtifactsMMO import Action
from src.custom_types.coordinates import Vector2


class MoveAction(Action):
    def __init__(self, position: Vector2 or None):
        Action.__init__(self, 'move')
        self._position: Vector2 or None = position

    @property
    def position(self) -> Vector2 or None:
        return self._position

    @position.setter
    def position(self, value: Vector2 or None):
        self._position = value

    def data(self):
        if not self._position:
            raise RuntimeError('No position set')

        return self._position.to_json()


class FightAction(Action):
    def __init__(self):
        Action.__init__(self, 'fight')

    def data(self):
        return None
