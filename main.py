# main.py
import asyncio
from config import config
from logger import logger
from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError, TelegramAPIError
from middleware.fsm_init import InitMiddlewareFSM
from handlers.app_start.start import router as app_start
from handlers.enter_app.enter_app import router as enter_app
from handlers.events_app.commands import router as command
from handlers.events_app.batton_menu import router as batton_menu
from handlers.events_app.events_text import router as event_text


# Инициализация
bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
dp.message.middleware(InitMiddlewareFSM())


# Основной цикл
async def main():
    try:
        dp.include_router(app_start)
        dp.include_router(enter_app)
        dp.include_router(command)
        dp.include_router(batton_menu)
        dp.include_router(event_text)
        await logger.info("Запуск бота...")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except TelegramNetworkError as e:
        await logger.error(f'Ошибка сети: {e}')
    except TelegramAPIError as e:
        await logger.error(f'Ошибка TelegramAPI: {e}')
    except Exception as e:
        await logger.exception(f"Непредвиденная ошибка: {e}")

    finally:
        await logger.info("Бот остановлен.")
        await logger.shutdown()
        await bot.session.close()


# Старт
if __name__ == "__main__":
    asyncio.run(main())