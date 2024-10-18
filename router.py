from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = (
        "Привет! Добро пожаловать! Нажми на кнопку ниже, чтобы запустить приложение."
    )

    web_app = types.WebAppInfo(url="https://bokko-twa.vercel.app/")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Запустить приложение", web_app=web_app)
        ]
    ])

    await message.answer(welcome_text, reply_markup=keyboard)
