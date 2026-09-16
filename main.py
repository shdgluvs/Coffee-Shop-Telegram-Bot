"""
Основной файл запуска Telegram-бота.
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, MenuButtonWebApp, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import BOT_TOKEN

logging.basicConfig(
    level=logging.WARNING,
    filename="bot_errors.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

web_app_info = WebAppInfo(url="https://dictator-morse-tiny.ngrok-free.dev")


@dp.message(Command("start"))
async def start_command(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Перейти в мини-приложение", 
            web_app=web_app_info,
        )
    )

    await message.answer(
        text="Приветствую. Мы работаем в мини-приложении. Перейдите, чтобы начать работу с нами.", 
        reply_markup=builder.as_markup(),
    ) 


async def main():
    menu_button = MenuButtonWebApp(
        type="web_app", 
        text="Перейти в мини-приложение", 
        web_app=web_app_info,
    )

    await bot.set_chat_menu_button(menu_button=menu_button)

    print("Бот успешно запущен и готов к работе.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())