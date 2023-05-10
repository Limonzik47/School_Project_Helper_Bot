from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#стартовое меню, нужно для ознакомления с политикой конфиденцинальности
kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b_start1 = KeyboardButton('Ознакомиться')
kb_start.row(b_start1)

#конект меню, подтверждение согласия или отказа от политики конфиденциальности
kb_acquaintance = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b_acquaintance1 = KeyboardButton('Сoгласен(на)')
# b_acquaintance2 = KeyboardButton('Не согласен(на)')
kb_acquaintance.add(b_acquaintance1)#b_acquaintance2)

# #меню повтора которое либо перезапускает политику либо останавливает бота
# kb_repeat = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
# b_repeat1 = KeyboardButton('Согласиться')
# b_repeat2 = KeyboardButton('Завершить')
# kb_repeat.row(b_repeat1,b_repeat2)

#основное меню
kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b_main1 = KeyboardButton('Информация')
b_main2 = KeyboardButton('Темы для проектов')
b_main3 = KeyboardButton('Cправочные материалы')
# b_main4 = KeyboardButton('Мой проект')
kb_main.row(b_main1,b_main2,b_main3)#.add(b_main4)


#выход в основное меню
b_general1 = KeyboardButton('Назад')
#выход из всех подменю в главное меню
b_general2 = KeyboardButton('Выход в главное меню')


# #меню мой проект
# kb_my_project = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True)
# b_my_project1 = KeyboardButton('Проект')
# b_my_project2 = KeyboardButton('Удалить выбранный проект')
# kb_my_project.row(b_my_project1, b_my_project2).add(b_general1)

#меню информации о боте
kb_info_bot = ReplyKeyboardMarkup(resize_keyboard=True)
b_info1 = KeyboardButton('Инфoрмaция')
b_info2 = KeyboardButton('Помощь')
b_info3 = KeyboardButton('Назад')
kb_info_bot.row(b_info1,b_info2,b_general1)

#меню помощи и службы поддержки
kb_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

b_help2 = KeyboardButton('Служба поддержки')
b_help3 = KeyboardButton('Нaзад')
kb_help.row(b_help2).add(b_help3)

#меню тем для проектов
kb_projects_thems = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b_projects_thems1 = KeyboardButton('Информатика')
b_projects_thems2 = KeyboardButton('Физика')
#...возможно дополнение
kb_projects_thems.row(b_projects_thems1,b_projects_thems2).add(b_general1)

#меню для справочных материалов
kb_reference_material = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b_reference_materials1 = KeyboardButton('Инфoрматика')
b_reference_materials2 = KeyboardButton('Физикa')
b_reference_materials3 = KeyboardButton('Требования')
#...возможно дополнение
kb_reference_material.row(b_reference_materials1,b_reference_materials2, b_reference_materials3).add(b_general1)

b_general_themes = KeyboardButton('Hазад к темам')


#темы проектов по информатике, деленные на столбцы по 10 штук в каждом
# kb_informatik_thems = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# b_informatik_thems1 = KeyboardButton('Стоблец 1')
# b_informatik_thems2 = KeyboardButton('Столбец 2')
# b_informatik_thems3 = KeyboardButton('Столбец 3')
# kb_informatik_thems.row(b_informatik_thems1,b_informatik_thems2,b_informatik_thems3).add(b_general_themes)

