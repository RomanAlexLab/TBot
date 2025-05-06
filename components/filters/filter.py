from aiogram.filters import Filter
from aiogram.types import Message
from components.provider.provider import provider_bot


class AdminFilter(Filter):
    async def __call__(self, message: Message):
        return  provider_bot.admin_filter(message.from_user.id)
