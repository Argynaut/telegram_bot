import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8081855051:AAHq3PmuVV-FNZT7QOOV7PwMh1YbBLYjsJQ"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()  

tasks = []

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! я бот который будет напоминать тебе о заданиях. Используй /add_task, чтобы добавить задачу и /list_tasks, чтобы их посмотреть.")

@dp.message(Command("add_task"))
async def add_task(message: Message):
    task = message.text[10:].strip()
    if task:
        tasks.append(task)
        await message.answer(f" Задача добавлена: {task}")
    else:
        await message.answer(" Напиши задачу после команды, например: `/add_task сделать дз`")

@dp.message(Command("list_tasks"))
async def list_tasks(message: Message):
    if tasks:
        task_list = "\n".join(f" {task}" for task in tasks)
        await message.answer(f" Твои задачи:\n{task_list}")
    else:
        await message.answer(" У тебя нет задач.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
