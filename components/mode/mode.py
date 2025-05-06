class ModeBot:
    def __init__(self):
        self.default: str = "default"
        self.game: str = "game"
        self.service: str = "service"
        self._step: int = 0  

    @property
    def step(self) -> int:
        return self._step

    @step.setter
    def step(self, value: int):
        try:
            if not (0 <= value <= 20):
                raise ValueError("step должно быть между 0 и 20")
            self._step = value
        except Exception as e:
            print(f"Ошибка в ModeBot->step.setter: {e}")


mode_bot = ModeBot()