# -*- coding: utf-8 -*-
import telebot
from telebot import types

def select_just_keyboard(data):
    keyboard = types.ReplyKeyboardMarkup()
    callback_button_help = types.KeyboardButton(text=data)
    keyboard.add(callback_button_help)
    return keyboard

def select_keyboard(k_type):
    if k_type == "cat-dog":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Собака", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Кошка", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # Вопросы которые относятся ко всем
    # шерсть
    if k_type == "haired":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Короткошерстная", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Длинношерстная", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # хвост
    if k_type == "tail":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Короткий", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Длинный", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # да-нет
    if k_type == "yes-no":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Нет", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Да", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # Вопросы для СОБАКИ
    # рост
    if k_type == "dog-height":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Менее 50см", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Более 50см", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # вес
    if k_type == "dog-weight":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Менее 50кг", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Более 50кг", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # рост
    if k_type == "dog-height-70":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Менее 70см", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Более 70см", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # уши
    if k_type == "dog-ears":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Короткие", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Длинные", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # тело
    if k_type == "dog-body":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Короткое", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Длинное", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard
    # Вопросы для КОТОВ
    # вес
    if k_type == "cat-weight":
        keyboard = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="Менее 6кг", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="Более 6кг", callback_data="2")
        keyboard.add(callback_button1, callback_button2)
        return keyboard