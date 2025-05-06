class CommandBot:
    """Команды"""
    help: str = "help"
    info: str = "info"
    admin: str = "admin"
    exit: str = "exit"

    """Системные команды"""
    _system_commands = ['help', 'info', 'admin', 'exit']

    def get_command_with_slash(self, command_name: str) -> str:
        """Метод для получения команд с добавлением слеша"""
        try:
            return f'/{getattr(self, command_name)}'
        
        except Exception as e:
            print(f"Ошибка в CommandBot.get_command_with_slash {e}")
            raise

    def get_system_commands(self) -> list[str]:
        """Возвращает список системных команд с добавлением слеша"""
        try:
            return [self.get_command_with_slash(cmd) for cmd in self._system_commands]
        
        except Exception as e:
            print(f"Ошибка в CommandBot.get_system_commands {e}")


commands_bot = CommandBot()