from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

web_app_info = WebAppInfo(
    url='https://www.youtube.com/watch?v=6QrF2eUt1KI',
)

My_Chanel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я подписался ️", callback_data='sub')],
    [InlineKeyboardButton(text="Subscribe to the channel", url="https://t.me/mvp1test")]
])

glav = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Go to the app💡", web_app=web_app_info)],
    [InlineKeyboardButton(text="Подробнее о проекте ⁉️", callback_data='more')],
    [InlineKeyboardButton(text="Профиль👤", callback_data='profile')],
    [InlineKeyboardButton(text="Наш канал", url="https://t.me/mvp1test")],
])



def cancel_keyboard():
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Отмена", callback_data='cancel')
    )
    return keyboard