from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


def get_start_keyboard():
    builder = InlineKeyboardBuilder()

    buttons = [
        ("Фармить звезды", "farm"),
        ("Профиль", "profile")
    ]

    for text, callback in buttons:
        builder.button(text=text, callback_data=callback)

    builder.adjust(2)
    return builder.as_markup()


@router.message(CommandStart())
async def cmd_start(message: Message):
    pass