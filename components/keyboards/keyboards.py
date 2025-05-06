from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)
from components.keyboards.placeholders import placeholder_k
from components.events.events import event_bot


# Тестовая клавиатура
test_keboard = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder=placeholder_k.reg,
    keyboard=[[KeyboardButton(text='Вариант 1')],
              [KeyboardButton(text='Вариант 2')]
              ])


# Стартовая клавиатура
start_keboard = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder=placeholder_k.reg,
    keyboard=[[KeyboardButton(text=event_bot.menu)]])


# Тестовая клавиатура
mode_keboard = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    input_field_placeholder=placeholder_k.reg,
    keyboard=[[KeyboardButton(text=event_bot.game)],
              [KeyboardButton(text=event_bot.service)],
              [KeyboardButton(text=event_bot.menu)]
              ])


# Продолжить
service_next = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[[KeyboardButton(text=event_bot.next)],
              ])


# Дверь или Портал
game_step_1 = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    keyboard=[[KeyboardButton(text=event_bot.portal)],
              [KeyboardButton(text=event_bot.dor)]
              ])


# Тестовая клавиатура
inline_game_step_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=event_bot.portal, callback_data='game_btn_1')],
    [InlineKeyboardButton(text=event_bot.dor, callback_data='game_btn_1')]
])
