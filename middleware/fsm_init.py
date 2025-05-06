from logger import logger
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from components.provider.provider import provider_bot
from components.mode.mode import mode_bot
from aiogram.exceptions import TelegramAPIError, TelegramNetworkError


# Инициализация значений FSM
class InitMiddlewareFSM(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[
            [Message,
             Dict[str, Any]],
             Awaitable[Any]
        ],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        try:
            # Получаем state и user данные
            state = data['state']
            user_data = await state.get_data()

            # Инициализируем FSM-данные, если их нет
            if not user_data:
                user = event.from_user

                # Обновляем данные
                await state.update_data(
                    user_id=user.id,
                    user_name=user.username,
                    user_full_name=user.full_name,
                    user_login = provider_bot.default_login,
                    user_password = provider_bot.default_password,
                    user_role=provider_bot.user,
                    user_mode=mode_bot.default,
                    step_mode=mode_bot._step
                )

            # Продолжаем обработку
            result = await handler(event, data)

        except TelegramNetworkError as e:
            await logger.error(f'Ошибка сети в InitMiddlewareFSM: {e}')
        except TelegramAPIError as e:
            await logger.error(f'Ошибка TelegramAPI в InitMiddlewareFSM: {e}')            
        except Exception as e:
            await logger.exception(f"Непредвиденная ошибка в InitMiddlewareFSM: {e}")

        return result