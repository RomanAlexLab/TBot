from asyncio import sleep
from logger import logger
from aiogram.types import Message
from abc import ABC, abstractmethod
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
import components.keyboards.keyboards as kb
from components.events.events import event_bot
from components.messages.messages import output_messages
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError


# Класс Observable (Издатель)
class ObservableTextEvent:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        """Добавить наблюдателя."""
        try:
            if observer not in self._observers:
                self._observers.append(observer)
        except Exception as e:
            print(f"Ошибка в ObservableTextEvent.add_observer: {e}")

    def remove_observer(self, observer):
        """Удалить наблюдателя."""
        try:
            if observer in self._observers:
                self._observers.remove(observer)
        except Exception as e:
            print(f"Ошибка в ObservableTextEvent.remove_observer: {e}")

    async def notify_observers(self, message: Message, state: FSMContext):
        """Уведомить всех наблюдателей о событии."""
        for observer in self._observers:
            try:
                await observer.update(message, state)

            except TelegramNetworkError as e:
                await logger.error(f'Ошибка сети в ObservableTextEvent.notify_observers: {e}')
            except TelegramAPIError as e:
                await logger.error(f'Ошибка TelegramAPI в ObservableTextEvent.notify_observers: {e}')
            except Exception as e:
                await logger.exception(f"Ошибка в ObservableTextEvent.notify_observers: {observer.__class__.__name__}: {e}")


#---------------------------------------------------

# НАБЛЮДАТЕЛИ СОБЫТИЙ

#---------------------------------------------------


# Базовый класс Observer (Наблюдатель)
class Observer(ABC):
    @abstractmethod
    async def update(self, message: Message, state: FSMContext):
        """Метод, который будет вызван при уведомлении."""
        pass


# Наблюдатель события \U0001F9E9 Игра
class GameObserver(Observer):
    def __init__(self):
        self.name = event_bot.game

    async def update(self, message: Message, state: FSMContext):
        """Обработка уведомления."""
        try:
            if message.text == self.name:
                await message.answer(output_messages.game_mes_1,
                    reply_markup=kb.game_step_1
                )

        except TelegramNetworkError as e:
            await logger.error(f'Ошибка сети в GameObserver.update: {e}')
        except TelegramAPIError as e:
            await logger.error(f'Ошибка TelegramAPI в GameObserver.update: {e}')
        except Exception as e:
            await logger.exception(f"Ошибка в GameObserver.update: {e}")


# Наблюдатель события дверь
class GameObserverDor(Observer):
    def __init__(self):
        self.name = event_bot.dor

    async def update(self, message: Message, state: FSMContext):
        """Обработка уведомления."""
        try:
            if message.text == self.name:
                await message.answer(output_messages.game_mes_2,
                    reply_markup=kb.start_keboard
                )

        except TelegramNetworkError as e:
            await logger.error(f'Ошибка сети в GameObserverDor.update: {e}')
        except TelegramAPIError as e:
            await logger.error(f'Ошибка TelegramAPI в GameObserverDor.update: {e}')
        except Exception as e:
            await logger.exception(f"Ошибка в GameObserverDor.update: {e}")


# Наблюдатель события портал
class GameObserverPortal(Observer):
    def __init__(self):
        self.name = event_bot.portal

    async def update(self, message: Message, state: FSMContext):
        """Обработка уведомления."""
        try:
            if message.text == self.name:
                await message.answer(output_messages.game_mes_3,
                    reply_markup=kb.start_keboard
                )

        except TelegramNetworkError as e:
            await logger.error(f'Ошибка сети в GameObserverPortal.update: {e}')
        except TelegramAPIError as e:
            await logger.error(f'Ошибка TelegramAPI в GameObserverPortal.update: {e}')
        except Exception as e:
            await logger.exception(f"Ошибка в GameObserverPortal.update: {e}")


# Наблюдатель события \U0001F50B Служебное
class ServiceObserverEvent(Observer):
    def __init__(self):
        self.name = event_bot.service

    async def update(self, message: Message, state: FSMContext):
        """Обработка уведомления."""
        try:
            if message.text == self.name:
                await message.answer(output_messages.service_mes_1,
                    reply_markup=kb.service_next
                )

        except TelegramNetworkError as e:
            await logger.error(f'Ошибка сети в ServiceObserverEvent.update: {e}')
        except TelegramAPIError as e:
            await logger.error(f'Ошибка TelegramAPI в ServiceObserverEvent.update: {e}')
        except Exception as e:
            await logger.exception(f"Ошибка в ServiceObserverEvent.update: {e}")


# Наблюдатель события Продолжить
class ServiсeObserverNext(Observer):
    def __init__(self):
        self.name = event_bot.next

    async def update(self, message: Message, state: FSMContext):
        """Обработка уведомления."""
        try:
            if message.text == self.name:
                # Уведомление что бот "печатает"
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(4)
                await message.answer(output_messages.service_mes_2)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(5)
                await message.answer(output_messages.service_mes_3)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(5)
                await message.answer(output_messages.service_mes_4)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(4)
                await message.answer(output_messages.service_mes_5)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(4)
                await message.answer(output_messages.service_mes_6)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(1)
                await message.answer(output_messages.service_mes_7)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(1)
                await message.answer(output_messages.service_mes_8)

                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await sleep(3)
                await message.answer(output_messages.service_mes_9,
                    reply_markup=kb.start_keboard
                )


        except TelegramNetworkError as e:
            await logger.error(f'Ошибка сети в ServiсeObserverNext.update: {e}')
        except TelegramAPIError as e:
            await logger.error(f'Ошибка TelegramAPI в ServiсeObserverNext.update: {e}')
        except Exception as e:
            await logger.exception(f"Ошибка в ServiсeObserverNext.update: {e}")


# Создаем издателя
observable_text = ObservableTextEvent()


# Создаем наблюдателей
game_observer = GameObserver()
game_observer_dor = GameObserverDor()
game_observer_portal = GameObserverPortal()
service_observer = ServiceObserverEvent()
service_observer_next = ServiсeObserverNext()


# Список наблюдателей
observers = [game_observer, game_observer_dor, 
             game_observer_portal, service_observer, 
             service_observer_next
            ]


# Подписываем всех наблюдателей
for observer in observers:
    observable_text.add_observer(observer)