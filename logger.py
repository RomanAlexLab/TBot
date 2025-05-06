# logger.py
from aiologger import Logger
from aiologger.formatters.base import Formatter
from aiologger.handlers.files import AsyncFileHandler

# Создаем асинхронный логгер
logger = Logger(name="bot_logger", level="INFO")

# Форматтер
formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Асинхронный хэндлер для записи в файл
handler = AsyncFileHandler(filename='bot.log', encoding='utf-8')
handler.formatter = formatter

# Добавляем хэндлер к логгеру
logger.add_handler(handler)