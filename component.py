from app_object import AppObject
from wire import Wire


class Component(AppObject):
    def __init__(self, position: tuple[int, int], size: int) -> None:
        super().__init__(position, size)
        # these are out wires, not in
        self.wires: list[Wire] = []
        self.outputs: list[bool] = []

    def power(self):
        pass

    def send_signal(self):
        for wire, output in zip(self.wires, self.outputs):
            if output:
                wire.power()
