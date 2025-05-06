from logger import logger
from aiogram import F, Router
from typing import List, Union
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from components.events.events import event_bot
from components.commands.commands import commands_bot
from components.system.system import system_attr_bot
from handlers.observers.text_event.text_event import observable_text
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError
from aiogram.enums import ChatAction


# Создание роутера
router = Router()


# Создание списка исключений (События исключения)
system_event: List[Union[str, None]] = (
    event_bot.get_system_events()
    + commands_bot.get_system_commands()
    + system_attr_bot.get_system_attr()
)


@router.message(~F.text.in_(system_event))
async def handle_all_text_except_commands(message: Message, state: FSMContext):
    """Обработка текстовых событий"""
    try:
        # Вызывыем обработчик текстовых сообщений
        await observable_text.notify_observers(message, state)

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в handle_all_text_except_commands: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в handle_all_text_except_commands: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в handle_all_text_except_commands: {e}")