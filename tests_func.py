import asyncio
from datetime import datetime
from aiogram.types import Message, Chat
from aiogram.fsm.context import FSMContext
from components.events.events import event_bot
from handlers.observers.text_event.text_event import observable_text
from components.commands.commands import commands_bot
from components.mode.mode import mode_bot
from components.provider.provider import provider_bot
from components.system.system import system_attr_bot


# Обработка событий
async def observable_func():
    chat = Chat(id=123456, type="private", first_name="TestUser")
    test_message = Message(
        message_id=1,
        date=datetime.now(),
        chat=chat,
        text=event_bot.game
    )
    test_fsm = FSMContext(storage='/d', key='none_key')
    await observable_text.notify_observers(test_message, test_fsm)


if __name__ == "__main__":
    print('---Системные команды---')
    print(commands_bot.get_system_commands())
    print('---Системные события---')
    print(event_bot.get_system_events())
    print('---Шаг режима---')
    mode_bot._step = 1
    print(mode_bot._step)
    print('---Вход в бота---')
    print(provider_bot.login(login='www'))
    print(provider_bot.password(password='qqq'))
    print(provider_bot.role(user_id=2345))
    print('---Систенмые атрибуты---')
    print(system_attr_bot.get_system_attr())
    #print('-----------------------------')
    #asyncio.run(observable_func())