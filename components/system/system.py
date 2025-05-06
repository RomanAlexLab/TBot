class SystemBotAttr:
    """Cистемные атрибуты бота"""
    none_attr_bot: None = None
    none_attr_bot_str: str = "None"

    """Системные события"""
    _system_attr = ['none_attr_bot', 'none_attr_bot_str']

    def get_system_attr(self) -> list[str]:
        """Возвращает список значений системных событий"""
        try:
            return [getattr(self, attr_bot) for attr_bot in self._system_attr]
        except Exception as e:
            print(f"Ошибка в SystemBotAttr.get_system_attr: {e}")


system_attr_bot = SystemBotAttr()