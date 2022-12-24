import asyncio
import wikipedia
from aiogram import Bot, Dispatcher, types

API_TOKEN = '5934321465:AAG18jOax4q_r4izYz1F1EUJVvI0OtSBS68'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

wikipedia.set_lang('ru')


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет!\n"
                         "Я умею искать для тебя нужную информацию на Википедии.\n"
                         "Список команд доступен по /help")


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer("/what_is request — краткая информация по запросу request\n"
                         "/top_search request — выдать топ-3 поиcковых запросов по request\n"
                         "/change_lang lang — сменить язык поиска на lang, где lang — это двухбуквенный "
                         "код страны. Например, ru, en, ua. По умолчанию поиск ведётся на русском\n"
                         "/help — список команд")


@dp.message_handler(commands=["what_is"])
async def cmd_what_is(message: types.Message):
    if not message.get_args():
        await message.answer("Пустой запрос")
    else:
        try:
            await message.answer(wikipedia.summary(message.get_args()))
        except wikipedia.exceptions.DisambiguationError as e:
            await message.answer("По вашему запросу ничего не нашлось :( Возможно, вы имели в виду:" + e.options[0])
        except:
            await message.answer("По вашему запросу ничего не нашлось :(")


@dp.message_handler(commands=["top_search"])
async def cmd_top_search(message: types.Message):
    if not message.get_args():
        await message.answer("Пустой запрос")
    else:
        try:
            await message.answer('\n'.join(wikipedia.search(message.get_args(), results=3)))
        except:
            await message.answer("По вашему запросу ничего не нашлось :(")


@dp.message_handler(commands=["change_lang"])
async def cmd_change_lang(message: types.Message):
    if not message.get_args():
        await message.answer("Пустой запрос")
    else:
        try:
            wikipedia.set_lang(message.get_args())
            await message.answer("Язык поиска успешно сменён")
        except:
            await message.answer("Некорректный код страны")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
