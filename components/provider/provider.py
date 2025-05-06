class Provider:
    """Вход и пользовательские роли"""
    def __init__(self):
        self.default_login = None
        self.default_password = None
        self.user: str = "User"
        self.admin: str = "Admin"
        self.admin_login = "www"
        self.admin_password = "qqq"
        self.list_admin: list = [1017764921]

    def login(self, login: str = None) -> bool:
        """Проверка логина"""
        try:
            return login == self.admin_login
        
        except Exception as e:
            print(f"Ошибка в Provider.login: {e}")

    def password(self, password: str = None) -> bool:
        """Проверка пароля"""
        try:
            return password == self.admin_password
        
        except Exception as e:
            print(f"Ошибка в Provider.password: {e}")

    def role(self, user_id: int = 0) -> str:
        """Проверка разрешения по User_id"""
        try:
            return self.admin if user_id in self.list_admin else self.user
        
        except Exception as e:
            print(f"Ошибка в Provider.role: {e}")

    def admin_filter(self, user_id: int = 0) -> bool:
        """Метод для фильтра"""
        try:
            return user_id in self.list_admin
        
        except Exception as e:
            print(f"Ошибка в Provider.admin_filter: {e}")


provider_bot = Provider()