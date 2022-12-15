from aiogram.types import ContentType, Message, InputFile, MediaGroup

from keyboards.inline import ikb_menu
from loader import dp

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def send_photo_file_id(message: Message):
    await message.reply(message.video.file_id)

@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    photo_file_id = "AgACAgIAAxkBAAIPC2Oa6v9KE2mlhkbcqTOAVTpTT2I4AAJXvTEbb23ZSG4dHoLg1hD9AQADAgADeAADLAQ"
    photo_url = "1wer"
    photo_bytes = InputFile(path_or_bytesio='media/copywriting.png')
    video_file_id = 'BAACAgIAAxkBAAIPHWOa7JlKl7Gn2sTqRjjmAn52k_QBAAJAHwACb23ZSBz8-sfY6u23LAQ'
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes, caption='Описание фото', reply_markup=ikb_menu)
    await dp.bot.send_video(chat_id=chat_id, video=video_file_id)

@dp.message_handler(text='/album')
async def send_photo(message: Message):
    album = MediaGroup()
    photo_file_id = "AgACAgIAAxkBAAIPC2Oa6v9KE2mlhkbcqTOAVTpTT2I4AAJXvTEbb23ZSG4dHoLg1hD9AQADAgADeAADLAQ"
    video_file_id = 'BAACAgIAAxkBAAIPHWOa7JlKl7Gn2sTqRjjmAn52k_QBAAJAHwACb23ZSBz8-sfY6u23LAQ'
    album.attach_photo(photo=photo_file_id)
    album.attach_video(video=video_file_id, caption='Описание всего альбома')
    await message.answer_media_group(media=album)