from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Сообщение', callback_data='Сообщение'),
                                        InlineKeyboardButton(text='ссылка', url='https://www.youtube.com/watch?v=2Il_Ab-s0W8')
                                    ],
                                ])