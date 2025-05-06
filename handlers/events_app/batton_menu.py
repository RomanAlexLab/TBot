from logger import logger
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import components.keyboards.keyboards as kb
from components.state_bot.state_bot import StateBot
from components.provider.provider import provider_bot
from components.messages.messages import output_messages
from components.commands.commands import commands_bot
from components.events.events import event_bot
from components.mode.mode import mode_bot
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError
from components.filters.filter import AdminFilter


# Создание роутера
router = Router()


@router.message(F.text == event_bot.menu)
async def batton_menu(message: Message, state: FSMContext):
    try:
        await state.set_state(StateBot.step_zero)
        await state.update_data(
            user_mode=mode_bot.default,
            step_mode=mode_bot._step
        )
        await message.answer(
                text=output_messages.menu_message,
                reply_markup=kb.mode_keboard
        )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в batton_menu: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в batton_menu: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в batton_menu: {e}")