class EventBot:
    """Cобытия"""
    menu: str = "\U0001F511 Меню"
    enter: str = "\U0001F511 Вход"
    reg: str = "\U0001F510 Регистрация"
    game: str = "\U0001F9E9 Игра"
    service: str = "\U0001F50B Служебное"
    next: str = "Продолжить"
    dor: str = "Дверь"
    portal: str = "Портал"

    """Системные события"""
    _system_events = ['menu', 'enter', 'reg']

    def get_system_events(self) -> list[str]:
        """Возвращает список значений системных событий"""
        try:
            return [getattr(self, event) for event in self._system_events]

        except Exception as e:
            print(f"Ошибка в EventBot.get_system_events {e}")


event_bot = EventBot()


if __name__ == "__main__":
    print(event_bot.get_system_events())