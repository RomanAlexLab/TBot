from logger import logger
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from components.provider.provider import provider_bot
from components.messages.messages import output_messages
from components.commands.commands import commands_bot
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError
from components.filters.filter import AdminFilter


# Создание роутера
router = Router()


# Команда /info
@router.message(AdminFilter(), Command(commands_bot.info))
async def info(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        role = data.get('user_role')
        if role == provider_bot.admin:
            await message.answer(
                    text=output_messages.info
            )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в info: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в info: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в info: {e}")


# Команда /help
@router.message(AdminFilter(), Command(commands_bot.info))
async def help(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        role = data.get('user_role')
        if role == provider_bot.admin:
            await message.answer(
                    text=output_messages.help
            )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в help: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в help: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в help: {e}")