from logger import logger
from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import components.keyboards.keyboards as kb
from aiogram.fsm.context import FSMContext
from components.messages.messages import output_messages
from components.state_bot.state_bot import StateBot
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError
from components.mode.mode import mode_bot


# Создание роутера
router = Router()


# /start
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    try:
        await state.set_state(StateBot.step_zero)
        await state.update_data(
            user_mode=mode_bot.default,
            step_mode=mode_bot._step
        )
        await message.answer(
                text=output_messages.start_message,
                reply_markup=kb.start_keboard
        )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в /star: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в /start: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в /start: {e}")