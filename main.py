# -*- coding: utf-8 -*-

import time
import telebot
from fysom import Fysom
import config
import response_storage
import utils

chat_id = ''
section_number = 0

# Массив финальных состояний
finals = ['first39', 'first41', 'first42', 'first43', 'first44', 'first48', 'first49', 'first50', 'first52', 'first53',
          'first54', 'first55', 'first56', 'second11', 'second13', 'second17', 'second18', 'second21', 'second22',
          'second23', 'second24', 'second25', 'second26', 'second27', 'second28', 'second29', 'second30', 'second31',
          'second32'
          ]

def create_fsm():
    # Создаем объект ДКА
    fsm = Fysom({'initial': 'waiting_start',  # начальное состояние
                 'events': [  # переходы
                     {'name': 'go_to_start', 'src': finals, 'dst': 'show_sections'},
                     {'name': 'gotstart', 'src': 'waiting_start', 'dst': 'show_sections'},
                     {'name': 'selected_first', 'src': 'show_sections', 'dst': 'first1'},
                     {'name': 'first1_first33', 'src': 'first1', 'dst': 'first33'},
                     {'name': 'first1_first34', 'src': 'first1', 'dst': 'first34'},
                     {'name': 'first33_first35', 'src': 'first33', 'dst': 'first35'},
                     {'name': 'first33_first36', 'src': 'first33', 'dst': 'first36'},
                     {'name': 'first34_first37', 'src': 'first34', 'dst': 'first37'},
                     {'name': 'first34_first38', 'src': 'first34', 'dst': 'first38'},
                     {'name': 'first35_first39', 'src': 'first35', 'dst': 'first39'},
                     {'name': 'first35_first40', 'src': 'first35', 'dst': 'first40'},
                     {'name': 'first36_first41', 'src': 'first36', 'dst': 'first41'},
                     {'name': 'first36_first42', 'src': 'first36', 'dst': 'first42'},
                     {'name': 'first37_first43', 'src': 'first37', 'dst': 'first43'},
                     {'name': 'first37_first44', 'src': 'first37', 'dst': 'first44'},
                     {'name': 'first38_first45', 'src': 'first38', 'dst': 'first45'},
                     {'name': 'first38_first46', 'src': 'first38', 'dst': 'first46'},
                     {'name': 'first40_first47', 'src': 'first40', 'dst': 'first47'},
                     {'name': 'first40_first48', 'src': 'first40', 'dst': 'first48'},
                     {'name': 'first45_first49', 'src': 'first45', 'dst': 'first49'},
                     {'name': 'first45_first50', 'src': 'first45', 'dst': 'first50'},
                     {'name': 'first46_first51', 'src': 'first46', 'dst': 'first51'},
                     {'name': 'first46_first52', 'src': 'first46', 'dst': 'first52'},
                     {'name': 'first47_first53', 'src': 'first47', 'dst': 'first53'},
                     {'name': 'first47_first54', 'src': 'first47', 'dst': 'first54'},
                     {'name': 'first51_first55', 'src': 'first51', 'dst': 'first55'},
                     {'name': 'first51_first56', 'src': 'first51', 'dst': 'first56'},

                     {'name': 'selected_second', 'src': 'show_sections', 'dst': 'second2'},
                     {'name': 'second2_second3', 'src': 'second2', 'dst': 'second3'},
                     {'name': 'second2_second4', 'src': 'second2', 'dst': 'second4'},
                     {'name': 'second3_second5', 'src': 'second3', 'dst': 'second5'},
                     {'name': 'second3_second6', 'src': 'second3', 'dst': 'second6'},
                     {'name': 'second4_second7', 'src': 'second4', 'dst': 'second7'},
                     {'name': 'second4_second8', 'src': 'second4', 'dst': 'second8'},
                     {'name': 'second5_second9', 'src': 'second5', 'dst': 'second9'},
                     {'name': 'second5_second10', 'src': 'second5', 'dst': 'second10'},
                     {'name': 'second6_second11', 'src': 'second6', 'dst': 'second11'},
                     {'name': 'second6_second12', 'src': 'second6', 'dst': 'second12'},
                     {'name': 'second7_second13', 'src': 'second7', 'dst': 'second13'},
                     {'name': 'second7_second14', 'src': 'second7', 'dst': 'second14'},
                     {'name': 'second8_second15', 'src': 'second8', 'dst': 'second15'},
                     {'name': 'second8_second16', 'src': 'second8', 'dst': 'second16'},
                     {'name': 'second9_second17', 'src': 'second9', 'dst': 'second17'},
                     {'name': 'second9_second18', 'src': 'second9', 'dst': 'second18'},
                     {'name': 'second10_second19', 'src': 'second10', 'dst': 'second19'},
                     {'name': 'second10_second20', 'src': 'second10', 'dst': 'second20'},
                     {'name': 'second12_second21', 'src': 'second12', 'dst': 'second21'},
                     {'name': 'second12_second22', 'src': 'second12', 'dst': 'second22'},
                     {'name': 'second14_second23', 'src': 'second14', 'dst': 'second23'},
                     {'name': 'second14_second24', 'src': 'second14', 'dst': 'second24'},
                     {'name': 'second15_second25', 'src': 'second15', 'dst': 'second25'},
                     {'name': 'second15_second26', 'src': 'second15', 'dst': 'second26'},
                     {'name': 'second16_second27', 'src': 'second16', 'dst': 'second27'},
                     {'name': 'second16_second28', 'src': 'second16', 'dst': 'second28'},
                     {'name': 'second19_second29', 'src': 'second19', 'dst': 'second29'},
                     {'name': 'second19_second30', 'src': 'second19', 'dst': 'second30'},
                     {'name': 'second20_second31', 'src': 'second20', 'dst': 'second31'},
                     {'name': 'second20_second32', 'src': 'second20', 'dst': 'second32'},
                 ],
                 'callbacks': {  # Коллбеки.Указываем какой метод будет отвечать за обработку какого события
                     'onwaiting_start': onwaiting_start,
                     'onshow_sections': onshow_sections,
                     'onfirst1': onfirst1,
                     'onfirst33': onfirst33,
                     'onfirst34': onfirst34,
                     'onfirst35': onfirst35,
                     'onfirst36': onfirst36,
                     'onfirst37': onfirst37,
                     'onfirst38': onfirst38,
                     'onfirst39': onfirst39,
                     'onfirst40': onfirst40,
                     'onfirst41': onfirst41,
                     'onfirst42': onfirst42,
                     'onfirst43': onfirst43,
                     'onfirst44': onfirst44,
                     'onfirst45': onfirst45,
                     'onfirst46': onfirst46,
                     'onfirst47': onfirst47,
                     'onfirst48': onfirst48,
                     'onfirst49': onfirst49,
                     'onfirst50': onfirst50,
                     'onfirst51': onfirst51,
                     'onfirst52': onfirst52,
                     'onfirst53': onfirst53,
                     'onfirst54': onfirst54,
                     'onfirst55': onfirst55,
                     'onfirst56': onfirst56,

                     'onsecond2': onsecond2,
                     'onsecond3': onsecond3,
                     'onsecond4': onsecond4,
                     'onsecond5': onsecond5,
                     'onsecond6': onsecond6,
                     'onsecond7': onsecond7,
                     'onsecond8': onsecond8,
                     'onsecond9': onsecond9,
                     'onsecond10': onsecond10,
                     'onsecond11': onsecond11,
                     'onsecond12': onsecond12,
                     'onsecond13': onsecond13,
                     'onsecond14': onsecond14,
                     'onsecond15': onsecond15,
                     'onsecond16': onsecond16,
                     'onsecond17': onsecond17,
                     'onsecond18': onsecond18,
                     'onsecond19': onsecond19,
                     'onsecond20': onsecond20,
                     'onsecond21': onsecond21,
                     'onsecond22': onsecond22,
                     'onsecond23': onsecond23,
                     'onsecond24': onsecond24,
                     'onsecond25': onsecond25,
                     'onsecond26': onsecond26,
                     'onsecond27': onsecond27,
                     'onsecond28': onsecond28,
                     'onsecond29': onsecond29,
                     'onsecond30': onsecond30,
                     'onsecond31': onsecond31,
                     'onsecond32': onsecond32
                }
    })
    return fsm

# Метод для формирования конечного ответа
def pet_description(image, number):
    sti = open(image, 'rb')
    breed = response_storage.select_message(section_number, number, 'answer')
    bot.send_photo(chat_id=chat_id,
                   photo=sti,
                   caption="Перед вами: <a href='https://ru.wikipedia.org/wiki/" + breed.replace(' ', '_') + "'>" + breed + "</a>",
                   parse_mode='HTML'
                   )
    # if fsm.current in finals:  # если текущее состояние является финальным, то
    #     fsm.go_to_start()  # переходим снова в начало к выбору ветки
    #     return

# Метод для формирования вопроса
def formation_of_a_request(key, number):
    keyboard = utils.select_keyboard(key)
    bot.send_message(chat_id=chat_id,
                     text=response_storage.select_message(section_number, number, 'question'),
                     reply_markup=keyboard)


#Метод для перехода на следующее состояние после набора команды "/start"
def change_state(state):
    if state == 'waiting_start':
        fsm.gotstart()

#Описываем работу обработчика события "onwaiting_start"
def onwaiting_start(e):
    @bot.message_handler(commands=["start"]) #атрибут отвечающие за реагирование на набор команды "/start"
    def start(message):
        bot.send_message(chat_id=message.chat.id,
                         text=response_storage.welcome_message) #берем текст сообщения из банка всех текстов(response_storage.py)
        global chat_id
        chat_id = message.chat.id
        fsm.current = 'waiting_start' #указываем, что текущее состояние - "waiting_start"
        change_state(fsm.current)

#Описываем работу обработчика события "onshow_sections"
def onshow_sections(e):
    keyboard = utils.select_keyboard("cat-dog")
    bot.send_message(chat_id=chat_id,
                     text=response_storage.first_response,
                     reply_markup=keyboard)

def onfirst1(e):
    formation_of_a_request("haired", 1)
def onfirst33(e):
    formation_of_a_request("dog-height", 3)
def onfirst34(e):
    formation_of_a_request("dog-height", 3)
def onfirst35(e):
    formation_of_a_request("tail", 2)
def onfirst36(e):
    formation_of_a_request("dog-weight", 4)
def onfirst37(e):
    formation_of_a_request("no-yes", 5)
def onfirst38(e):
    formation_of_a_request("dog-height-70", 6)
def onfirst39(e):
    pet_description('dog/Английский_бульдог.jpeg', 1)
    # bot.send_message(chat_id=chat_id,
    #                  text=breed
    #                  )
def onfirst40(e):
    formation_of_a_request("dog-ears", 7)
def onfirst41(e):
    pet_description('dog/angliyskiy-fokskhaund.jpg', 5)
def onfirst42(e):
    pet_description('dog/Датский_дог.jpg', 6)
def onfirst43(e):
    pet_description('dog/Ирландский_красный_сеттер.jpg', 7)
def onfirst44(e):
    pet_description('dog/English_Cocker_Spaniel.jpg', 8)
def onfirst45(e):
    formation_of_a_request("dog-ears", 7)
def onfirst46(e):
    formation_of_a_request("yes-no", 9)
def onfirst47(e):
    formation_of_a_request("dog-body", 8)
def onfirst48(e):
    pet_description('dog/гончая.jpg', 4)
def onfirst49(e):
    pet_description('dog/Колли.jpg', 9)
def onfirst50(e):
    pet_description('dog/Большой_вандейский_грифон.jpg', 10)
def onfirst51(e):
    formation_of_a_request("yes-no", 10)
def onfirst52(e):
    pet_description('dog/Сенбернар.jpg', 13)
def onfirst53(e):
    pet_description('dog/Мопс.jpg', 2)
def onfirst54(e):
    pet_description('dog/Chihuahua.jpg', 3)
def onfirst55(e):
    pet_description('dog/Ньюфаундленд.jpg', 11)
def onfirst56(e):
    pet_description('dog/Ирландский_волкодав.jpg', 12)


def onsecond2(e):
    formation_of_a_request("haired", 1)
def onsecond3(e):
    formation_of_a_request("cat-weight", 2)
def onsecond4(e):
    formation_of_a_request("cat-weight", 2)
def onsecond5(e):
    formation_of_a_request("tail", 3)
def onsecond6(e):
    formation_of_a_request("yes-no", 4)
def onsecond7(e):
    formation_of_a_request("yes-no", 4)
def onsecond8(e):
    formation_of_a_request("tail", 3)
def onsecond9(e):
    formation_of_a_request("yes-no", 5)
def onsecond10(e):
    formation_of_a_request("yes-no", 6)
def onsecond11(e):
    pet_description('cat/Саванна.jpg', 7)
def onsecond12(e):
    formation_of_a_request("yes-no", 7)
def onsecond13(e):
    pet_description('cat/Persialainen.jpg', 10)
def onsecond14(e):
    formation_of_a_request("yes-no", 6)
def onsecond15(e):
    formation_of_a_request("yes-no", 8)
def onsecond16(e):
    formation_of_a_request("yes-no", 4)
def onsecond17(e):
    pet_description('cat/JapaneseBobtail.jpg', 14)
def onsecond18(e):
    pet_description('cat/Пиксибоб.jpg', 2)
def onsecond19(e):
    formation_of_a_request("yes-no", 7)
def onsecond20(e):
    formation_of_a_request("yes-no", 4)
def onsecond21(e):
    pet_description('cat/Kartezianskaya-koshka.jpg', 8)
def onsecond22(e):
    pet_description('cat/Chausie.jpg', 9)
def onsecond23(e):
    pet_description('cat/british_longhair.jpg', 11)
def onsecond24(e):
    pet_description('cat/Шотландская_вислоухая_кошка.jpg', 12)
def onsecond25(e):
    pet_description('cat/Kurilian_Bobtail.jpg', 13)
def onsecond26(e):
    pet_description('cat/american_bobtail.jpg', 1)
def onsecond27(e):
    pet_description('cat/Norvezhskaja.jpg', 15)
def onsecond28(e):
    pet_description('cat/Мейн-кун.jpg', 16)
def onsecond29(e):
    pet_description('cat/Тайская_кошка.jpg', 3)
def onsecond30(e):
    pet_description('cat/Абиссинская.jpg', 4)
def onsecond31(e):
    pet_description('cat/Британская_короткошёрстная.jpg', 5)
def onsecond32(e):
    pet_description('cat/Шотландская_вислоухая_кошка.jpg', 6)

#Создаем объект бота
bot = telebot.TeleBot(config.token) #передаем в параметр уникальный токен нашего бота
print(bot)
fsm = create_fsm()
#Обработчик всех нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    data = call.data #получаем значение, соответствующее кнопки(нажал кнопку 5 - получил в call.data значение 5).
    #Далее, в соответствии с текущим состоянием(fsm.current) и значением, полученным после нажатия на кнопку,
    # указываем в какое состояние необходимо перейти
    if fsm.current == 'show_sections':
        global section_number
        section_number = int(data)
        if section_number == 1:
            fsm.selected_first()
            return
        if section_number == 2:
            fsm.selected_second()
            return
    if fsm.current == 'first1':
        if data == '1':
            fsm.first1_first33()
            return
        if data == '2':
            fsm.first1_first34()
            return
    if fsm.current == 'first33':
        if data == '1':
            fsm.first33_first35()
            return
        if data == '2':
            fsm.first33_first36()
            return
    if fsm.current == 'first34':
        if data == '1':
            fsm.first34_first37()
            return
        if data == '2':
            fsm.first34_first38()
            return
    if fsm.current == 'first35':
        if data == '1':
            fsm.first35_first39()
            return
        if data == '2':
            fsm.first35_first40()
            return
    if fsm.current == 'first36':
        if data == '1':
            fsm.first36_first41()
            return
        if data == '2':
            fsm.first36_first42()
            return
    if fsm.current == 'first37':
        if data == '1':
            fsm.first37_first43()
            return
        if data == '2':
            fsm.first37_first44()
            return
    if fsm.current == 'first38':
        if data == '1':
            fsm.first38_first45()
            return
        if data == '2':
            fsm.first38_first46()
            return
    if fsm.current == 'first40':
        if data == '1':
            fsm.first40_first47()
            return
        if data == '2':
            fsm.first40_first48()
            return
    if fsm.current == 'first45':
        if data == '1':
            fsm.first45_first49()
            return
        if data == '2':
            fsm.first45_first50()
            return
    if fsm.current == 'first46':
        if data == '1':
            fsm.first46_first51()
            return
        if data == '2':
            fsm.first46_first52()
            return
    if fsm.current == 'first47':
        if data == '1':
            fsm.first47_first53()
            return
        if data == '2':
            fsm.first47_first54()
            return
    if fsm.current == 'first51':
        if data == '1':
            fsm.first51_first55()
            return
        if data == '2':
            fsm.first51_first56()
            return

    if fsm.current == 'second2':
        if data == '1':
            fsm.second2_second3()
            return
        if data == '2':
            fsm.second2_second4()
            return
    if fsm.current == 'second3':
        if data == '1':
            fsm.second3_second5()
            return
        if data == '2':
            fsm.second3_second6()
            return
    if fsm.current == 'second4':
        if data == '1':
            fsm.second4_second7()
            return
        if data == '2':
            fsm.second4_second8()
            return
    if fsm.current == 'second5':
        if data == '1':
            fsm.second5_second9()
            return
        if data == '2':
            fsm.second5_second10()
            return
    if fsm.current == 'second6':
        if data == '1':
            fsm.second6_second11()
            return
        if data == '2':
            fsm.second6_second12()
            return
    if fsm.current == 'second7':
        if data == '1':
            fsm.second7_second13()
            return
        if data == '2':
            fsm.second7_second14()
            return
    if fsm.current == 'second8':
        if data == '1':
            fsm.second8_second15()
            return
        if data == '2':
            fsm.second8_second16()
            return
    if fsm.current == 'second9':
        if data == '1':
            fsm.second9_second17()
            return
        if data == '2':
            fsm.second9_second18()
            return
    if fsm.current == 'second10':
        if data == '1':
            fsm.second10_second19()
            return
        if data == '2':
            fsm.second10_second20()
            return
    if fsm.current == 'second12':
        if data == '1':
            fsm.second12_second21()
            return
        if data == '2':
            fsm.second12_second22()
            return
    if fsm.current == 'second14':
        if data == '1':
            fsm.second14_second23()
            return
        if data == '2':
            fsm.second14_second24()
            return
    if fsm.current == 'second15':
        if data == '1':
            fsm.second15_second25()
            return
        if data == '2':
            fsm.second15_second26()
            return
    if fsm.current == 'second16':
        if data == '1':
            fsm.second16_second27()
            return
        if data == '2':
            fsm.second16_second28()
            return
    if fsm.current == 'second19':
        if data == '1':
            fsm.second19_second29()
            return
        if data == '2':
            fsm.second19_second30()
            return
    if fsm.current == 'second20':
        if data == '1':
            fsm.second20_second31()
            return
        if data == '2':
            fsm.second20_second32()
            return

if __name__ == '__main__':
   #В бесконечном цикле держмим бот в запущенном состоянии, обрабатывая возможные ошибки.
    while True:
        try:
            bot.polling(none_stop=True, timeout=1000)
        except Exception as ex:
            print(ex)
            time.sleep(10)




