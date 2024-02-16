import asyncio

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from sqlalchemy import insert
from db.model import User
from bot.buttons.reply import menu_btn, menu_btn_start
from db.connect import session
from dispatcher import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message, state : FSMContext) -> None:
    await message.answer(f"Assalomu alaykum ! , {hbold(message.from_user.full_name)}!")
    query = insert(User).values(chat_id=message.from_user.id , username = message.from_user.full_name)
    session.execute(query)
    session.commit()
    await message.answer(f"Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi" , reply_markup=menu_btn())


@dp.message(lambda msg : msg.text == 'Filial 📍')
async def echo_handler(msg: Message):
    pass

@dp.message(lambda msg : msg.text == 'Start ✅')
async def echo_handler(msg: Message):
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿" , reply_markup=menu_btn_start())

@dp.message(lambda msg : msg.text == 'News')
async def echo_handler(msg: Message):
    await msg.answer(reply_markup=get_info())


#
#

import httpx
from bs4 import BeautifulSoup
async def get_info():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.fitnessblender.com/")
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    for i in soup.find_all("div", {"class": "vue cards"}):
        title : str = i.find('h2', {'class': 'category'})
        name : str = i.find('h1', {'class': 'content-title'})
        date : str = i.find('div', {'class': 'primary-detail'})
        p : str = i.find('div', {'class': 'content-actions-msg'})

        new = ""
        if title:
            new += title.text + "\n"
        if name :
            new += name.text + "\n"
        if date :
            new += date.text + "\n"
        if p:
            new += p.text
        return new

