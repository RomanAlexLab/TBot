import pytest
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from unittest.mock import AsyncMock, MagicMock
from components.state_bot.state_bot import StateBot
from components.mode.mode import mode_bot
from handlers.app_start.start import cmd_start
from handlers.enter_app.enter_app import enter_admin
from components.messages.messages import output_messages
from components.keyboards import keyboards as kb
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError


# Фикстура для message
@pytest.fixture
def mock_message():
    message = AsyncMock(spec=Message)
    message.answer = AsyncMock()
    return message

# Фикстура для state
@pytest.fixture
def mock_state():
    state = AsyncMock(spec=FSMContext)
    state.set_state = AsyncMock()
    state.update_data = AsyncMock()
    return state


# /start
@pytest.mark.asyncio
async def test_cmd_start_success(mock_message, mock_state):
    # Вызов функции
    await cmd_start(mock_message, mock_state)

    # Проверки
    mock_state.set_state.assert_called_once_with(StateBot.step_zero)
    mock_state.update_data.assert_called_once_with(
        user_mode=mode_bot.default,
        step_mode=mode_bot._step
    )
    mock_message.answer.assert_called_once_with(
        text=output_messages.start_message,
        reply_markup=kb.start_keboard
    )


# /admin
@pytest.mark.asyncio
async def test_enter_admin_success(mock_message, mock_state):
    # Вызов функции
    await enter_admin(mock_message, mock_state)

    # Проверки
    mock_state.set_state.assert_called_once_with(StateBot.login)
    mock_message.answer.assert_called_once_with(
        text=output_messages.enter_login
    )