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
from components.filters.filter import AdminFilter
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError


# Создание роутера
router = Router()


# Команда /admin или событие \U0001F511 Вход
@router.message(Command(commands_bot.admin))
@router.message(F.text == event_bot.enter)
async def enter_admin(message: Message, state: FSMContext):
    try:
        await state.set_state(StateBot.login)
        await message.answer(
                text=output_messages.enter_login
        )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в enter_admin: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в enter_admin: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в enter_admin: {e}")


# Сохраниение логина и предложение вести пароль
@router.message(StateBot.login)
async def flow_login(message: Message, state: FSMContext):
    try:
        await state.update_data(user_login=message.text)
        await state.set_state(StateBot.password)
        await message.answer(output_messages.enter_password)

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в flow_login: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI flow_login: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка flow_login: {e}")


# Сохраниение пароля и обработка информации
@router.message(StateBot.password)
async def flow_password(message: Message, state: FSMContext):
    try:
        # Сбор информации
        await state.update_data(user_password=message.text)
        data = await state.get_data()
        login = data.get('user_login')
        password = data.get('user_password')

        if provider_bot.login(login=login) \
        and provider_bot.password(password=password) \
        and provider_bot.role(user_id=message.from_user.id) == provider_bot.admin:
            # Доступ разрешён
            await state.set_state(StateBot.step_zero)
            await state.update_data(user_role=provider_bot.admin)
            await state.update_data(user_login=provider_bot.default_login)
            await state.update_data(user_password=provider_bot.default_password)
            await message.answer(output_messages.access_allow)
        
        else:
            # Доступ запрещён
            await message.answer(output_messages.access_denied)
            await state.update_data(user_role=provider_bot.user)
            await state.set_state(StateBot.step_zero)
            await message.answer(
                    text=output_messages.command_enter_admin
            )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в flow_password: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в flow_password: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка flow_password: {e}")


# Команда /exit
@router.message(AdminFilter(), Command(commands_bot.exit))
async def exit_admin(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        role = data.get('user_role')
        if role == provider_bot.admin:
            await state.set_state(StateBot.step_zero)
            await state.update_data(
                user_role=provider_bot.user,
                user_mode=mode_bot.default,
                step_mode=mode_bot._step
            )
            await message.answer(
                    text=output_messages.exit_admin,
                    reply_markup=kb.start_keboard
            )

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети в exit_admin: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI в exit_admin: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка в exit_admin: {e}")