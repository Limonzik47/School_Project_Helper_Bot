from create_bot import dp

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext

#база данных

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///client.dp')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    action_time = Column(DateTime)

Base.metadata.create_all(engine)

SessionMakerClass = sessionmaker(bind=engine)
session = SessionMakerClass()




from aiogram import types


from keyboard.client_keyboard import kb_start
from keyboard.client_keyboard import kb_acquaintance
from keyboard.client_keyboard import kb_main
# from keyboard.client_keyboard import kb_repeat
from keyboard.client_keyboard import kb_info_bot
from keyboard.client_keyboard import kb_help
from keyboard.client_keyboard import kb_projects_thems
from keyboard.client_keyboard import kb_reference_material

# from keyboard.client_keyboard import kb_informatik_thems
# from keyboard.client_keyboard import kb_my_project
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#ФИЗИКА
from handlers.subjects.physicali_sub import physical_thems
from handlers.subjects.physicali_sub import back_thems

from handlers.subjects.physicali_sub import physical_thems_stolb1
from handlers.subjects.physicali_sub import physical_thems_stolb2
from handlers.subjects.physicali_sub import physical_thems_stolb3

from handlers.subjects.physicali_sub import continit_stolb1
from handlers.subjects.physicali_sub import continit_stolb2

from handlers.subjects.physicali_sub import stolb1_physical_thems1
from handlers.subjects.physicali_sub import stolb1_physical_thems2
from handlers.subjects.physicali_sub import stolb1_physical_thems3
from handlers.subjects.physicali_sub import stolb1_physical_thems4
from handlers.subjects.physicali_sub import stolb1_physical_thems5
from handlers.subjects.physicali_sub import stolb1_physical_thems6
from handlers.subjects.physicali_sub import stolb1_physical_thems7
from handlers.subjects.physicali_sub import stolb1_physical_thems8
from handlers.subjects.physicali_sub import stolb1_physical_thems9
from handlers.subjects.physicali_sub import stolb1_physical_thems10
from handlers.subjects.physicali_sub import stolb2_physical_thems11
from handlers.subjects.physicali_sub import stolb2_physical_thems12
from handlers.subjects.physicali_sub import stolb2_physical_thems13
from handlers.subjects.physicali_sub import stolb2_physical_thems14
from handlers.subjects.physicali_sub import stolb2_physical_thems15
from handlers.subjects.physicali_sub import stolb2_physical_thems16
from handlers.subjects.physicali_sub import stolb2_physical_thems17
from handlers.subjects.physicali_sub import stolb2_physical_thems18
from handlers.subjects.physicali_sub import stolb2_physical_thems19
from handlers.subjects.physicali_sub import stolb2_physical_thems20
from handlers.subjects.physicali_sub import stolb3_physical_thems21
from handlers.subjects.physicali_sub import stolb3_physical_thems22
from handlers.subjects.physicali_sub import stolb3_physical_thems23
from handlers.subjects.physicali_sub import stolb3_physical_thems24
from handlers.subjects.physicali_sub import stolb3_physical_thems25
from handlers.subjects.physicali_sub import stolb3_physical_thems26
from handlers.subjects.physicali_sub import stolb3_physical_thems27
from handlers.subjects.physicali_sub import stolb3_physical_thems28
from handlers.subjects.physicali_sub import stolb3_physical_thems29
from handlers.subjects.physicali_sub import stolb3_physical_thems30

from handlers.subjects.physicali_sub import stolb1_physical_thems_back1
from handlers.subjects.physicali_sub import stolb2_physical_thems_back2
from handlers.subjects.physicali_sub import stolb3_physical_thems_back3

from handlers.subjects.physicali_sub import physical_themes_1
from handlers.subjects.physicali_sub import physical_themes_2
from handlers.subjects.physicali_sub import physical_themes_3
from handlers.subjects.physicali_sub import physical_themes_4
from handlers.subjects.physicali_sub import physical_themes_5
from handlers.subjects.physicali_sub import physical_themes_6
from handlers.subjects.physicali_sub import physical_themes_7
from handlers.subjects.physicali_sub import physical_themes_8
from handlers.subjects.physicali_sub import physical_themes_9
from handlers.subjects.physicali_sub import physical_themes_10
from handlers.subjects.physicali_sub import physical_themes_11
from handlers.subjects.physicali_sub import physical_themes_12
from handlers.subjects.physicali_sub import physical_themes_13
from handlers.subjects.physicali_sub import physical_themes_14
from handlers.subjects.physicali_sub import physical_themes_15
from handlers.subjects.physicali_sub import physical_themes_16
from handlers.subjects.physicali_sub import physical_themes_17
from handlers.subjects.physicali_sub import physical_themes_18
from handlers.subjects.physicali_sub import physical_themes_19
from handlers.subjects.physicali_sub import physical_themes_20
from handlers.subjects.physicali_sub import physical_themes_21
from handlers.subjects.physicali_sub import physical_themes_22
from handlers.subjects.physicali_sub import physical_themes_23
from handlers.subjects.physicali_sub import physical_themes_24
from handlers.subjects.physicali_sub import physical_themes_25
from handlers.subjects.physicali_sub import physical_themes_26
from handlers.subjects.physicali_sub import physical_themes_27
from handlers.subjects.physicali_sub import physical_themes_28
from handlers.subjects.physicali_sub import physical_themes_29
from handlers.subjects.physicali_sub import physical_themes_30

from handlers.subjects.physicali_sub import back_physical_themes_1
from handlers.subjects.physicali_sub import back_physical_themes_2
from handlers.subjects.physicali_sub import back_physical_themes_3



#ИНФОРМАТИКА

from handlers.subjects.informatika_sub import informatika_thems
from handlers.subjects.informatika_sub import back_thems

from handlers.subjects.informatika_sub import informatika_thems_stolb1
from handlers.subjects.informatika_sub import informatika_thems_stolb2
from handlers.subjects.informatika_sub import informatika_thems_stolb3

from handlers.subjects.informatika_sub import continit_stolb3
from handlers.subjects.informatika_sub import continit_stolb4

from handlers.subjects.informatika_sub import stolb1_informatika_thems1
from handlers.subjects.informatika_sub import stolb1_informatika_thems2
from handlers.subjects.informatika_sub import stolb1_informatika_thems3
from handlers.subjects.informatika_sub import stolb1_informatika_thems4
from handlers.subjects.informatika_sub import stolb1_informatika_thems5
from handlers.subjects.informatika_sub import stolb1_informatika_thems6
from handlers.subjects.informatika_sub import stolb1_informatika_thems7
from handlers.subjects.informatika_sub import stolb1_informatika_thems8
from handlers.subjects.informatika_sub import stolb1_informatika_thems9
from handlers.subjects.informatika_sub import stolb1_informatika_thems10
from handlers.subjects.informatika_sub import stolb2_informatika_thems11
from handlers.subjects.informatika_sub import stolb2_informatika_thems12
from handlers.subjects.informatika_sub import stolb2_informatika_thems13
from handlers.subjects.informatika_sub import stolb2_informatika_thems14
from handlers.subjects.informatika_sub import stolb2_informatika_thems15
from handlers.subjects.informatika_sub import stolb2_informatika_thems16
from handlers.subjects.informatika_sub import stolb2_informatika_thems17
from handlers.subjects.informatika_sub import stolb2_informatika_thems18
from handlers.subjects.informatika_sub import stolb2_informatika_thems19
from handlers.subjects.informatika_sub import stolb2_informatika_thems20
from handlers.subjects.informatika_sub import stolb3_informatika_thems21
from handlers.subjects.informatika_sub import stolb3_informatika_thems22
from handlers.subjects.informatika_sub import stolb3_informatika_thems23
from handlers.subjects.informatika_sub import stolb3_informatika_thems24
from handlers.subjects.informatika_sub import stolb3_informatika_thems25
from handlers.subjects.informatika_sub import stolb3_informatika_thems26
from handlers.subjects.informatika_sub import stolb3_informatika_thems27
from handlers.subjects.informatika_sub import stolb3_informatika_thems28
from handlers.subjects.informatika_sub import stolb3_informatika_thems29
from handlers.subjects.informatika_sub import stolb3_informatika_thems30

from handlers.subjects.informatika_sub import stolb1_informatika_thems_back1
from handlers.subjects.informatika_sub import stolb2_informatika_thems_back2
from handlers.subjects.informatika_sub import stolb3_informatika_thems_back3

from handlers.subjects.informatika_sub import informatika_themes_1
from handlers.subjects.informatika_sub import informatika_themes_2
from handlers.subjects.informatika_sub import informatika_themes_3
from handlers.subjects.informatika_sub import informatika_themes_4
from handlers.subjects.informatika_sub import informatika_themes_5
from handlers.subjects.informatika_sub import informatika_themes_6
from handlers.subjects.informatika_sub import informatika_themes_7
from handlers.subjects.informatika_sub import informatika_themes_8
from handlers.subjects.informatika_sub import informatika_themes_9
from handlers.subjects.informatika_sub import informatika_themes_10
from handlers.subjects.informatika_sub import informatika_themes_11
from handlers.subjects.informatika_sub import informatika_themes_12
from handlers.subjects.informatika_sub import informatika_themes_13
from handlers.subjects.informatika_sub import informatika_themes_14
from handlers.subjects.informatika_sub import informatika_themes_15
from handlers.subjects.informatika_sub import informatika_themes_16
from handlers.subjects.informatika_sub import informatika_themes_17
from handlers.subjects.informatika_sub import informatika_themes_18
from handlers.subjects.informatika_sub import informatika_themes_19
from handlers.subjects.informatika_sub import informatika_themes_20
from handlers.subjects.informatika_sub import informatika_themes_21
from handlers.subjects.informatika_sub import informatika_themes_22
from handlers.subjects.informatika_sub import informatika_themes_23
from handlers.subjects.informatika_sub import informatika_themes_24
from handlers.subjects.informatika_sub import informatika_themes_25
from handlers.subjects.informatika_sub import informatika_themes_26
from handlers.subjects.informatika_sub import informatika_themes_27
from handlers.subjects.informatika_sub import informatika_themes_28
from handlers.subjects.informatika_sub import informatika_themes_29
from handlers.subjects.informatika_sub import informatika_themes_30


from handlers.subjects.informatika_sub import back_informatika_themes_1
from handlers.subjects.informatika_sub import back_informatika_themes_2
from handlers.subjects.informatika_sub import back_informatika_themes_3


# from handlers.subjects.physicali_sub import my_project
# from handlers.subjects.physicali_sub import project
# from handlers.subjects.physicali_sub import delete_project

from handlers.subjects.physicali_sub import select_project

pdf_project = None

#START#
@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    await message.answer(f'Приветствую! Я <b>School Project Helper Bot</b> – бот, который поможет вам определиться с темой вашего проекта и предоставит план действий.'
                         f' Для того <b>чтобы продолжить</b> работу с ботом <b>необходимо ознакомиться с политикой конфиденциальности</b>.', parse_mode='html', reply_markup=kb_start)

@dp.message_handler(lambda message : 'Ознакомиться' in message.text)
async def acquaintance(message : types.Message):
    await message.answer(f'<b>Политика конфиденциальности:</b>\n\n'
                         f'Эта политика конфиденциальности описывает, как ваша информация <b>собирается</b>, <b>используется</b> и <b>передается</b> ботом.\n'
                         f'Используя Бота, <b>вы соглашаетесь</b> с условиями данной политики.\n\n'
                         f'<b>Сбор данных:</b>\n\n'
                         f'Бот <b>собирает</b> следующие данные:\n\n'
                         f'<b>1. </b>Имя пользователя.\n'
                         f'<b>2. </b>История чата.\n'
                         f'<b>3. </b>Содержание сообщения.\n'
                         f'<b>4. </b>Иные данные, добровольно предоставленные пользователем.\n\n'
                         f'<b>Использование данных:</b>\n\nДанные, собранные ботом, <b>используются</b> для следующих целей:\n\n'
                         f'<b>1. </b>Для улучшения услуг, предоставляемых Ботом.\n'
                         f'<b>2. </b>Чтобы персонализировать пользовательский опыт.\n'
                         f'<b>3. </b>Для ответа на запросы и проблемы пользователей.\n\n'
                         f'<b>Обмен данными:</b> \n\nБот <b>не передает</b> пользовательские <b>данные</b> третьим лицам, <b>за исключением</b> следующих обстоятельств:\n\n'
                         f'<b>1. </b>Когда это необходимо для целей предоставления услуг Бота.\n'
                         f'<b>2. </b>При явной авторизации пользователем.\n\n'
                         f'<b>Изменения в политике:</b> эта политика конфиденциальности<b> может</b> время от времени <b>обновляться</b>. '
                         f'Мы уведомим пользователей о любых существенных изменениях политики.', parse_mode='html', reply_markup=kb_acquaintance)

    # await message.answer('<b>С политикой...</b>', parse_mode='html', reply_markup=kb_acquaintance)

# @dp.message_handler(lambda message : 'Согласиться' in message.text)
# async def agree(message : types.Message):
#     await message.answer(f'Привет, <b>{message.from_user.username}!</b> \n\n'
#                          f'<b>Приступим!</b>\n\n'
#                          f'Бот может помочь вам с выбором темы для вашего проекта, а также предложит вам план выполнения,'
#                          f' еще в боте присутствуют справочные материалы которые могут оказаться полезными для вас. \n\n'
#                          f'<b>Важное замечание</b> все темы не постоянны, те или иные пункты в них могут меняться, об обновлениях тем бот вас уведомит.'
#                          f' Также вы можете задать некоторые вопросы боту через чат, но учтите что <b>бот не всегда сможет вас понять</b>.'
#                          f' Для удобной работы с ботом воспользуйтесь меню.', parse_mode='html',reply_markup=kb_main)

# @dp.message_handler(lambda message : 'Не согласен(на)' in message.text)
# async def refuse(message : types.Message):
#     await message.answer(f'Доступ к нашему Telegram боту будет доступен только после согласия с нашей политикой конфиденциальности.', parse_mode='html', reply_markup= kb_repeat)
#
# @dp.message_handler(lambda message : 'Завершить' in message.text)
# async def end(message : types.Message, state : FSMContext):
#     await message.answer(f'<b>Вы всегда можете вернуться!</b>\n'
#                          f'Чтобы вернуться необходимо ввести команду <b>start</b>', parse_mode='html')
#     await state.finish()

@dp.message_handler(lambda message : 'Сoгласен(на)' in message.text)
async def main(message : types.Message):
    # User = User(username = message.from_user.username,action_time = DateTime.now())
    # session.add(User)
    # session.commit()
    await message.answer(f'Привет, <b>{message.from_user.username}!</b> \n\n'
                         f'<b>Приступим!</b>\n\n'
                         f'Бот может помочь вам с выбором темы для вашего проекта, а также предложит вам план выполнения,'
                         f' еще в боте присутствуют справочные материалы которые могут оказаться полезными для вас. \n\n'
                         f'<b>Важное замечание</b> все темы не постоянны, те или иные пункты в них могут меняться, об обновлениях тем бот вас уведомит.'
                         f' Для удобной работы с ботом воспользуйтесь меню.', parse_mode='html',reply_markup=kb_main)
    # last_action = session.query(User).filter_by(username = message.from_user.username).order_by(User.action_time.desc()).first()
    # if last_action:
    #     await message.answer(f'Вы дали согласие в {last_action.action_time}')

#MAIN MENU#

###########################################INFO#######################################################

##INFO##
@dp.message_handler(lambda message : 'Информация' in message.text)
async def info_bot(message : types.Message):
    await message.answer(f'<b>Добро пожаловать в меню информации!</b>\n\n'
                         f'Здесь вы найдете полезные сведения и ответы на различные вопросы.'
                         f' Держите руку на пульсе и оставайтесь в курсе!', parse_mode='html', reply_markup=kb_info_bot)

@dp.message_handler(lambda message : 'Инфoрмaция' in message.text)
async def info(message : types.Message):
    await message.answer((f'Полное название проекта: <b>School Project Helper Bot</b>\n'
                          f'Разработчик: <b>Limonzik47</b>\n'
                          f'Дата выхода Beta-версии: <b>09.05.2023</b>\n'
                          f'История обновлений:<b> обновлений еще не было</b>\n'), parse_mode='html', reply_markup=kb_info_bot)

##BACK##
@dp.message_handler(lambda message : 'Назад' in message.text)
async def back_info_bot(message : types.Message):
    await message.answer(f'<b>Шаг назад</b>', parse_mode='html', reply_markup= kb_main)

##HELP##

ib_help = InlineKeyboardMarkup(row_width=2)
b_help = InlineKeyboardButton(text='Пройти опрос', url='https://docs.google.com/forms/d/e/1FAIpQLSda5EeNsrG0_g9zNjLVhvixa1a13R8Ppc-CtFDq8KJziico3A/viewform?usp=sf_link')
ib_help.row(b_help)

@dp.message_handler(lambda message : 'Помощь' in message.text)
async def help(message : types.Message):
    await message.answer(f'<b>Добро пожаловать в меню помощи нашего телеграм бота!</b>\n\n'
                         f'Ознакомьтесь с нашими функциями и получите полезные советы по работе с ботом.'
                         f' Если у вас возникнут какие-либо вопросы, мы всегда готова помочь вам в решении проблем.', parse_mode='html', reply_markup= kb_help)
    await message.answer(f'<b>Вы можете помочь нам</b> улучшить работу нашего бота<b> пройдя опрос.</b>', parse_mode='html', reply_markup=ib_help)



##BACK HELP##
@dp.message_handler(lambda message : 'Нaзад' in message.text)
async def back_info(message : types.Message):
    await message.answer(f'<b>Шаг назад</b>', parse_mode='html', reply_markup= kb_info_bot)

ib_serv = InlineKeyboardMarkup(row_width=2)
b_serv = InlineKeyboardButton(text='Написать', url='https://t.me/kimyoushitnabouken')
ib_serv.row(b_serv)
#HELP_SERVICE#
@dp.message_handler(lambda message : 'Служба поддержки' in message.text)
async def help_service(message : types.Message):
    await message.answer(f'<b>Добро пожаловать в меню службы поддержки!</b>\n\n'
                         f'Здесь вы можете получить помощь по любым вопросам и проблемам, связанными с использованием нашего телеграм бота.'
                         f' Чтобы связаться с нашей поддержкой, пожалуйста, выберите один из вариантов ниже:', parse_mode='html', reply_markup= kb_help)
    await message.answer(f'<b>Отправьте электронное письмо на нашу почту:</b>\n\nschoolprojecthelperbot@gmail.com', parse_mode='html')
    await message.answer(f'<b>Свяжитесь с нами напрямую через Telegram</b>',parse_mode='html' ,reply_markup=ib_serv)



###############MY_PROJECT###################
# @dp.message_handler(lambda message : 'Мой проект' in message.text)
# async def my_project(message : types.Message):
#     await message.answer('Ваш проект', reply_markup= kb_my_project )
# @dp.message_handler(lambda message : 'Проект' in message.text)
# async def project(message : types.Message):
#     global select_project
#     if select_project:
#         await message.answer('Ваш проект:\n' + select_project, reply_markup= kb_my_project)
#     else:
#         await message.answer('Вы еще не определились с проектом', reply_markup= kb_my_project)
# @dp.message_handler(lambda message : 'Удалить выбранный проект' in message.text)
# async def delete_project(message : types.Message):
#     global select_project
#     select_project = None
#     await message.answer('Выбранная тема удалена', reply_markup=kb_my_project)



#######################################THEMS FOR PROJECTS#############################################

@dp.message_handler(lambda message : 'Темы для проектов' in message.text)
async def themes_for_project(message : types.Message):
    await message.answer(f'<b>Добро пожаловать в раздел Темы для проектов!</b>\n\nЗдесь вы можите найти темы для своих проектов по интерисующим вас предметам.', parse_mode='html', reply_markup= kb_projects_thems)

####INFORMATIKA THEMS####


# @dp.message_handler(lambda message : 'Информатика' in message.text)
# async def informatik_thems(message : types.Message):
#     await message.answer(f'30 тем проектов по информатике и план к ним', parse_mode='html', reply_markup= kb_informatik_thems)

@dp.message_handler(lambda message : 'Hазад к темам' in message.text)
async def back_info_bot(message : types.Message):
    await message.answer(f'<b>Шаг назад</b>', parse_mode='html', reply_markup= kb_projects_thems)





####PHYSICAL THEMS####






#############################################REFERENCE MATERIALS#######################################

@dp.message_handler(lambda message : 'Cправочные материалы' in message.text)
async def reference_material(message : types.Message):
    await message.answer(f'<b>Добро пожаловать в меню Справочные материалы!</b>\n\nЗдесь вы можете найти <b>полезные теоретические материалы,</b> которые могут пригодиться при созднаии вашего проекта.', parse_mode='html', reply_markup= kb_reference_material)




#######INFORMATIKA########
@dp.message_handler(lambda message : 'Инфoрматика' in message.text)
async def reference_informat(message : types.Message):
    await message.answer(f'<b>Справочные материалы по информатике</b>\n\n'
                         f'Пока что тут пусто, но не время растраиваться, возможно в следующем обновление все появится!\n\n'
                         f''
                         f''
                         f'', parse_mode='html', reply_markup= kb_reference_material)

#######PHYSICAL###########
@dp.message_handler(lambda message : 'Физикa' in message.text)
async def reference_physical(message : types.Message):
    await message.answer(f'<b>Справочные материалы по физике</b>\n\n'
                         f'Пока что тут пусто, но не время растраиваться, возможно в следующем обновление все появится!\n\n'
                         f''
                         f''
                         f'', parse_mode='html', reply_markup= kb_reference_material)

######ТРЕБОВАНИЯ##########
@dp.message_handler(lambda message : 'Требования' in message.text)
async def reference_req(message : types.Message):
    await message.answer(f'<b>Требования по оформлению проекта</b>\n\n'
                         f'<b>Параметры страниц проекта</b>\n\n'
                         f'Текст проекта печатается на листах формата А4 с одной стороны.\n'
                         f'Поля:\n'
                         f'-левое поле листа - 20 мм\n'
                         f'-правое - 10 мм\n-'
                         f'-верхнее и нижнее - 15 мм\n\n'
                         f'Текст набирается шрифтом: Times New Roman.\n'
                         f'Размер шрифта: 14.\n'
                         f'Интервал: полуторный.\n'
                         f'Текст на странице: выравнивается по ширине.\n\n'
                         f'<b>Оформление титульного листа проекта</b>\n\n'
                         f'Титульный лист творческого проекта оформляется на листе формата А4.\n'
                         f'Поля:\n'
                         f'-левое поле листа - 20 мм\n'
                         f'-правое - 10 мм\n'
                         f'-верхнее и нижнее - 15 мм\n'
                         f'Междустрочный интервал – 1,5\n'
                         f'Номер страницы на титульном листе не ставится!\n'
                         f'В верхнем поле титульного листа проекта указывается полное название образовательного учреждения (размер шрифта – 16 пт.).\n'
                         f'В среднем поле (посередине листа) пишется «Проект» (шрифт – 24 пт.)\n'
                         f'На следующей строке – заглавными буквами название работы без слова "тема", без кавычек и без точки в конце предложения (шрифт – 28 пт.).\n'
                         f'В правом нижнем углу титульного листа работы указываются сведения об авторе проекта (фамилия, имя, класс),'
                         f' о руководителе проекта (пишется «Руководитель» и указываются его фамилия, инициалы и должность (шрифт – 14 пт.).\n'
                         f'В случае, если руководителей работы несколько, указываются все. Если есть консультанты проекта, то их фамилии помещаются ниже руководителя с указанием «Консультант».\n'
                         f'В самом нижнем поле содержания титульного листа проекта по центру пишется место выполнения проекта, а на следующей строчке – год выполнения работы без точки, кавычек, "год" или "г" (шрифт – 14 пт.).\n\n'
                         f''
                         f'<b>Заголовки в проектной работе</b>\n\n'
                         f'Заголовок печатается полужирным шрифтом с заглавной буквы, не подчеркивается,'
                         f' точка в конце не ставится. Переносы слов в заголовках глав не допускаются. Между заголовком и текстом делается отступ 2 интервала.\n'
                         f'Каждая глава творческого проекта начинается с новой страницы. Нумеруются главы арабскими цифрами.\n'
                         f'Параграфы нумеруются цифрами через точку, где первая цифра – номер главы, вторая – номер параграфа.\n'
                         f'Если параграфы имеют тоже пункты, то их нумеруют соответственно тремя цифрами через точку.\n'
                         f''
                         f'Если упоминаете в тексте проектной работы фамилии других людей: авторов, ученых, исследователей и т.п., то их инициалы пишутся в начале фамилии.\n\n'
                         f''
                         f'<b>Оформление приложений проекта</b>\n\n'
                         f'Согласно правил оформления творческих проектов, рисунки, фотографии, графики, диаграммы, чертежи, эскизы,'
                         f' таблицы должны быть расположены и оформлены в конце описания проектной работы после Списка литературы на отдельных страницах в приложениях.\n\n'
                         f''
                         f'<b>Нумерация страниц творческого проекта</b>\n\n'
                         f'После завершения набора творческой работы следует пронумеровать страницы. Номера страниц ставятся начиная с цифры 2 со второй страницы. На первой номер не ставится. Расположение нумерации - внизу по центру.\n'
                         f'Не допускается использование в оформлении проектной работы или творческого проекта рамок и других элементов для украшения.\n\n'
                         f''
                         f'<b>Общий план проекта</b>\n\n'
                         f'1. Титульный лист проекта.\n'
                         f'2. Содержание проекта.\n'
                         f'3. Введение проекта.\n'
                         f'4. Историческая справка по проблеме проекта.\n'
                         f'5. Технологическая часть проекта.\n'
                         f'6. Экономическое обоснование проекта, расчеты.\n'
                         f'7. Экологическое обоснование проекта.\n'
                         f'8. Новые знания и умения, полученные при выполнении проекта.\n'
                         f'10. Заключение проекта.\n'
                         f'11. Список литературы проекта.\n'
                         f'12. Приложения проекта.\n'
                         f'', parse_mode='html', reply_markup= kb_reference_material)




def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(acquaintance)
    dp.register_message_handler(main)
    # dp.register_message_handler(agree)
    # dp.register_message_handler(refuse)
    # dp.register_message_handler(end)
    dp.register_message_handler(info_bot)
    dp.register_message_handler(info)
    dp.register_message_handler(back_info_bot)
    dp.register_message_handler(help)

    dp.register_message_handler(back_info)
    dp.register_message_handler(help_service)
    dp.register_message_handler(themes_for_project)
    dp.register_message_handler(reference_material)
    dp.register_message_handler(reference_informat)
    dp.register_message_handler(reference_physical)
    dp.register_message_handler(reference_req)

    dp.register_message_handler(physical_thems)
    dp.register_message_handler(back_thems)

    dp.register_message_handler(physical_thems_stolb1)
    dp.register_message_handler(physical_thems_stolb2)
    dp.register_message_handler(physical_thems_stolb3)

    dp.register_message_handler(continit_stolb1)
    dp.register_message_handler(continit_stolb2)

    dp.register_message_handler(stolb1_physical_thems1)
    dp.register_message_handler(stolb1_physical_thems2)
    dp.register_message_handler(stolb1_physical_thems3)
    dp.register_message_handler(stolb1_physical_thems4)
    dp.register_message_handler(stolb1_physical_thems5)
    dp.register_message_handler(stolb1_physical_thems6)
    dp.register_message_handler(stolb1_physical_thems7)
    dp.register_message_handler(stolb1_physical_thems8)
    dp.register_message_handler(stolb1_physical_thems9)
    dp.register_message_handler(stolb1_physical_thems10)
    dp.register_message_handler(stolb2_physical_thems11)
    dp.register_message_handler(stolb2_physical_thems12)
    dp.register_message_handler(stolb2_physical_thems13)
    dp.register_message_handler(stolb2_physical_thems14)
    dp.register_message_handler(stolb2_physical_thems15)
    dp.register_message_handler(stolb2_physical_thems16)
    dp.register_message_handler(stolb2_physical_thems17)
    dp.register_message_handler(stolb2_physical_thems18)
    dp.register_message_handler(stolb2_physical_thems19)
    dp.register_message_handler(stolb2_physical_thems20)
    dp.register_message_handler(stolb3_physical_thems21)
    dp.register_message_handler(stolb3_physical_thems22)
    dp.register_message_handler(stolb3_physical_thems23)
    dp.register_message_handler(stolb3_physical_thems24)
    dp.register_message_handler(stolb3_physical_thems25)
    dp.register_message_handler(stolb3_physical_thems26)
    dp.register_message_handler(stolb3_physical_thems27)
    dp.register_message_handler(stolb3_physical_thems28)
    dp.register_message_handler(stolb3_physical_thems29)
    dp.register_message_handler(stolb3_physical_thems30)

    dp.register_message_handler(stolb1_physical_thems_back1)
    dp.register_message_handler(stolb2_physical_thems_back2)
    dp.register_message_handler(stolb3_physical_thems_back3)

    dp.register_message_handler(physical_themes_1)
    dp.register_message_handler(physical_themes_2)
    dp.register_message_handler(physical_themes_3)
    dp.register_message_handler(physical_themes_4)
    dp.register_message_handler(physical_themes_5)
    dp.register_message_handler(physical_themes_6)
    dp.register_message_handler(physical_themes_7)
    dp.register_message_handler(physical_themes_8)
    dp.register_message_handler(physical_themes_9)
    dp.register_message_handler(physical_themes_10)
    dp.register_message_handler(physical_themes_11)
    dp.register_message_handler(physical_themes_12)
    dp.register_message_handler(physical_themes_13)
    dp.register_message_handler(physical_themes_14)
    dp.register_message_handler(physical_themes_15)
    dp.register_message_handler(physical_themes_16)
    dp.register_message_handler(physical_themes_17)
    dp.register_message_handler(physical_themes_18)
    dp.register_message_handler(physical_themes_19)
    dp.register_message_handler(physical_themes_20)
    dp.register_message_handler(physical_themes_21)
    dp.register_message_handler(physical_themes_22)
    dp.register_message_handler(physical_themes_23)
    dp.register_message_handler(physical_themes_24)
    dp.register_message_handler(physical_themes_25)
    dp.register_message_handler(physical_themes_26)
    dp.register_message_handler(physical_themes_27)
    dp.register_message_handler(physical_themes_28)
    dp.register_message_handler(physical_themes_29)
    dp.register_message_handler(physical_themes_30)

    dp.register_message_handler(back_physical_themes_1)
    dp.register_message_handler(back_physical_themes_2)
    dp.register_message_handler(back_physical_themes_3)

    # dp.register_message_handler(my_project)
    # dp.register_message_handler(project)
    # dp.register_message_handler(delete_project)

    dp.register_message_handler(informatika_thems)

    dp.register_message_handler(informatika_thems_stolb1)
    dp.register_message_handler(informatika_thems_stolb2)
    dp.register_message_handler(informatika_thems_stolb3)

    dp.register_message_handler(continit_stolb3)
    dp.register_message_handler(continit_stolb4)

    dp.register_message_handler(stolb1_informatika_thems1)
    dp.register_message_handler(stolb1_informatika_thems2)
    dp.register_message_handler(stolb1_informatika_thems3)
    dp.register_message_handler(stolb1_informatika_thems4)
    dp.register_message_handler(stolb1_informatika_thems5)
    dp.register_message_handler(stolb1_informatika_thems6)
    dp.register_message_handler(stolb1_informatika_thems7)
    dp.register_message_handler(stolb1_informatika_thems8)
    dp.register_message_handler(stolb1_informatika_thems9)
    dp.register_message_handler(stolb1_informatika_thems10)
    dp.register_message_handler(stolb2_informatika_thems11)
    dp.register_message_handler(stolb2_informatika_thems12)
    dp.register_message_handler(stolb2_informatika_thems13)
    dp.register_message_handler(stolb2_informatika_thems14)
    dp.register_message_handler(stolb2_informatika_thems15)
    dp.register_message_handler(stolb2_informatika_thems16)
    dp.register_message_handler(stolb2_informatika_thems17)
    dp.register_message_handler(stolb2_informatika_thems18)
    dp.register_message_handler(stolb2_informatika_thems19)
    dp.register_message_handler(stolb2_informatika_thems20)
    dp.register_message_handler(stolb3_informatika_thems21)
    dp.register_message_handler(stolb3_informatika_thems22)
    dp.register_message_handler(stolb3_informatika_thems23)
    dp.register_message_handler(stolb3_informatika_thems24)
    dp.register_message_handler(stolb3_informatika_thems25)
    dp.register_message_handler(stolb3_informatika_thems26)
    dp.register_message_handler(stolb3_informatika_thems27)
    dp.register_message_handler(stolb3_informatika_thems28)
    dp.register_message_handler(stolb3_informatika_thems29)
    dp.register_message_handler(stolb3_informatika_thems30)

    dp.register_message_handler(stolb1_informatika_thems_back1)
    dp.register_message_handler(stolb2_informatika_thems_back2)
    dp.register_message_handler(stolb3_informatika_thems_back3)

    dp.register_message_handler(informatika_themes_1)
    dp.register_message_handler(informatika_themes_2)
    dp.register_message_handler(informatika_themes_3)
    dp.register_message_handler(informatika_themes_4)
    dp.register_message_handler(informatika_themes_5)
    dp.register_message_handler(informatika_themes_6)
    dp.register_message_handler(informatika_themes_7)
    dp.register_message_handler(informatika_themes_8)
    dp.register_message_handler(informatika_themes_9)
    dp.register_message_handler(informatika_themes_10)
    dp.register_message_handler(informatika_themes_11)
    dp.register_message_handler(informatika_themes_12)
    dp.register_message_handler(informatika_themes_13)
    dp.register_message_handler(informatika_themes_14)
    dp.register_message_handler(informatika_themes_15)
    dp.register_message_handler(informatika_themes_16)
    dp.register_message_handler(informatika_themes_17)
    dp.register_message_handler(informatika_themes_18)
    dp.register_message_handler(informatika_themes_19)
    dp.register_message_handler(informatika_themes_20)
    dp.register_message_handler(informatika_themes_21)
    dp.register_message_handler(informatika_themes_22)
    dp.register_message_handler(informatika_themes_23)
    dp.register_message_handler(informatika_themes_24)
    dp.register_message_handler(informatika_themes_25)
    dp.register_message_handler(informatika_themes_26)
    dp.register_message_handler(informatika_themes_27)
    dp.register_message_handler(informatika_themes_28)
    dp.register_message_handler(informatika_themes_29)
    dp.register_message_handler(informatika_themes_30)

    dp.register_message_handler(back_informatika_themes_1)
    dp.register_message_handler(back_informatika_themes_2)
    dp.register_message_handler(back_informatika_themes_3)















