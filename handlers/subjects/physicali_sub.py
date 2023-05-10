import datetime

#Занос в базу данных#



select_project = None


#прочие импорты
from create_bot import dp, bot
from aiogram import types

#клава моих проектов
# from keyboard.client_keyboard import kb_my_project

#физика-клавы
from keyboard.client_keyboard import kb_projects_thems

from keyboard.key_subjects.b_key_physical import ib_physical_thems

from keyboard.key_subjects.b_key_physical import ib_stolb1_physical_thems

from keyboard.key_subjects.b_key_physical import ib_physical_thems_1
from keyboard.key_subjects.b_key_physical import ib_physical_thems_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_4
from keyboard.key_subjects.b_key_physical import ib_physical_thems_5
from keyboard.key_subjects.b_key_physical import ib_physical_thems_6
from keyboard.key_subjects.b_key_physical import ib_physical_thems_7
from keyboard.key_subjects.b_key_physical import ib_physical_thems_8
from keyboard.key_subjects.b_key_physical import ib_physical_thems_9
from keyboard.key_subjects.b_key_physical import ib_physical_thems_10

from keyboard.key_subjects.b_key_physical import ib_full_thems_1
from keyboard.key_subjects.b_key_physical import ib_full_thems_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_4
from keyboard.key_subjects.b_key_physical import ib_full_thems_5
from keyboard.key_subjects.b_key_physical import ib_full_thems_6
from keyboard.key_subjects.b_key_physical import ib_full_thems_7
from keyboard.key_subjects.b_key_physical import ib_full_thems_8
from keyboard.key_subjects.b_key_physical import ib_full_thems_9
from keyboard.key_subjects.b_key_physical import ib_full_thems_10

from keyboard.key_subjects.b_key_physical import ib_stolb2_physical_thems

from keyboard.key_subjects.b_key_physical import ib_physical_thems_1_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_2_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_3_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_4_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_5_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_6_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_7_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_8_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_9_2
from keyboard.key_subjects.b_key_physical import ib_physical_thems_10_2

from keyboard.key_subjects.b_key_physical import ib_full_thems_1_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_2_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_3_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_4_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_5_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_6_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_7_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_8_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_9_2
from keyboard.key_subjects.b_key_physical import ib_full_thems_10_2

from keyboard.key_subjects.b_key_physical import ib_stolb3_physical_thems

from keyboard.key_subjects.b_key_physical import ib_physical_thems_1_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_2_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_3_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_4_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_5_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_6_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_7_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_8_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_9_3
from keyboard.key_subjects.b_key_physical import ib_physical_thems_10_3

from keyboard.key_subjects.b_key_physical import ib_full_thems_1_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_2_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_3_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_4_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_5_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_6_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_7_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_8_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_9_3
from keyboard.key_subjects.b_key_physical import ib_full_thems_10_3



#физика-текста
from title.physical_text import ph_sp_1
from title.physical_text import ph_sp_2
from title.physical_text import ph_sp_3
from title.physical_text import ph_t_1
from title.physical_text import ph_t_2
from title.physical_text import ph_t_3
from title.physical_text import ph_t_4
from title.physical_text import ph_t_5
from title.physical_text import ph_t_6
from title.physical_text import ph_t_7
from title.physical_text import ph_t_8
from title.physical_text import ph_t_9
from title.physical_text import ph_t_10
from title.physical_text import ph_t_11
from title.physical_text import ph_t_12
from title.physical_text import ph_t_13
from title.physical_text import ph_t_14
from title.physical_text import ph_t_15
from title.physical_text import ph_t_16
from title.physical_text import ph_t_17
from title.physical_text import ph_t_18
from title.physical_text import ph_t_19
from title.physical_text import ph_t_20
from title.physical_text import ph_t_21
from title.physical_text import ph_t_22
from title.physical_text import ph_t_23
from title.physical_text import ph_t_24
from title.physical_text import ph_t_25
from title.physical_text import ph_t_26
from title.physical_text import ph_t_27
from title.physical_text import ph_t_28
from title.physical_text import ph_t_29
from title.physical_text import ph_t_30

from title.physical_text import ph_t_1_2
from title.physical_text import ph_t_2_2
from title.physical_text import ph_t_3_2
from title.physical_text import ph_t_4_2
from title.physical_text import ph_t_5_2
from title.physical_text import ph_t_6_2
from title.physical_text import ph_t_7_2
from title.physical_text import ph_t_8_2
from title.physical_text import ph_t_9_2
from title.physical_text import ph_t_10_2
from title.physical_text import ph_t_11_2
from title.physical_text import ph_t_12_2
from title.physical_text import ph_t_13_2
from title.physical_text import ph_t_14_2
from title.physical_text import ph_t_15_2
from title.physical_text import ph_t_16_2
from title.physical_text import ph_t_17_2
from title.physical_text import ph_t_18_2
from title.physical_text import ph_t_19_2
from title.physical_text import ph_t_20_2
from title.physical_text import ph_t_21_2
from title.physical_text import ph_t_22_2
from title.physical_text import ph_t_23_2
from title.physical_text import ph_t_24_2
from title.physical_text import ph_t_25_2
from title.physical_text import ph_t_26_2
from title.physical_text import ph_t_27_2
from title.physical_text import ph_t_28_2
from title.physical_text import ph_t_29_2
from title.physical_text import ph_t_30_2




#вывод меню со списками
@dp.message_handler(lambda message : 'Физика' in message.text)
async def physical_thems(message : types.Message):
    await message.answer(f'<b>Темы для проектов по физике</b>', parse_mode='html',
                         reply_markup= ib_physical_thems)


#выход из списков
@dp.callback_query_handler(text='backa4')
async def back_thems(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text='<b>Возвращение к предметам</b>', parse_mode='html',
                           reply_markup=kb_projects_thems)
    await callback_query.answer()


#открытие списков
@dp.callback_query_handler(text='a1')
async def physical_thems_stolb1(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id,text=ph_sp_1, parse_mode='html', reply_markup= ib_stolb1_physical_thems)
    await callback_query.answer()

@dp.callback_query_handler(text='a2')
async def physical_thems_stolb2(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text= ph_sp_2, parse_mode='html', reply_markup=ib_stolb2_physical_thems)

@dp.callback_query_handler(text='a3')
async def physical_thems_stolb3(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text= ph_sp_3, parse_mode='html', reply_markup=ib_stolb3_physical_thems)
    await callback_query.answer()



#переход от списка к списку
@dp.callback_query_handler(text='continie1')
async def continit_stolb1(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text= ph_sp_2,reply_markup= ib_stolb2_physical_thems)
    await callback_query.answer()

@dp.callback_query_handler(text='continie2')
async def continit_stolb2(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text= ph_sp_3, reply_markup=ib_stolb3_physical_thems)
    await callback_query.answer()



#физика-темы
@dp.callback_query_handler(text='1')
async def stolb1_physical_thems1(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_1, reply_markup=ib_physical_thems_1)
     await callback_query.answer()

@dp.callback_query_handler(text='2')
async def stolb1_physical_thems2(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text = ph_t_2, parse_mode='html',
                                   reply_markup=ib_physical_thems_2)
    await callback_query.answer()

@dp.callback_query_handler(text='3')
async def stolb1_physical_thems3(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_3, parse_mode='html',
                                   reply_markup=ib_physical_thems_3)

@dp.callback_query_handler(text='4')
async def stolb1_physical_thems4(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_4, parse_mode='html',
                                   reply_markup=ib_physical_thems_4)
     await callback_query.answer()

@dp.callback_query_handler(text='5')
async def stolb1_physical_thems5(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_5, parse_mode='html',
                                   reply_markup=ib_physical_thems_5)
     await callback_query.answer()

@dp.callback_query_handler(text='6')
async def stolb1_physical_thems6(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_6, parse_mode='html',
                                   reply_markup=ib_physical_thems_6)
     await callback_query.answer()

@dp.callback_query_handler(text='7')
async def stolb1_physical_thems7(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_7, parse_mode='html',
                                   reply_markup=ib_physical_thems_7)
     await callback_query.answer()

@dp.callback_query_handler(text='8')
async def stolb1_physical_thems8(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_8, parse_mode='html',
                                   reply_markup=ib_physical_thems_8)
     await callback_query.answer()

@dp.callback_query_handler(text='9')
async def stolb1_physical_thems9(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_9, parse_mode='html',
                                   reply_markup=ib_physical_thems_9)
     await callback_query.answer()


@dp.callback_query_handler(text='10')
async def stolb1_physical_thems10(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_10, parse_mode='html',
                                   reply_markup=ib_physical_thems_10)
    await callback_query.answer()

@dp.callback_query_handler(text='11')
async def stolb2_physical_thems11(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_11,
                            reply_markup=ib_physical_thems_1_2)
     await callback_query.answer()

@dp.callback_query_handler(text='12')
async def stolb2_physical_thems12(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text = ph_t_12, parse_mode='html',
                                   reply_markup=ib_physical_thems_2_2)
    await callback_query.answer()

@dp.callback_query_handler(text='13')
async def stolb2_physical_thems13(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_13, parse_mode='html',
                                   reply_markup=ib_physical_thems_3_2)
    await callback_query.answer()

@dp.callback_query_handler(text='14')
async def stolb2_physical_thems14(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_14, parse_mode='html',
                                   reply_markup=ib_physical_thems_4_2)
     await callback_query.answer()

@dp.callback_query_handler(text='15')
async def stolb2_physical_thems15(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_15, parse_mode='html',
                                   reply_markup=ib_physical_thems_5_2)
     await callback_query.answer()

@dp.callback_query_handler(text='16')
async def stolb2_physical_thems16(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_16, parse_mode='html',
                                   reply_markup=ib_physical_thems_6_2)
     await callback_query.answer()

@dp.callback_query_handler(text='17')
async def stolb2_physical_thems17(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_17, parse_mode='html',
                                   reply_markup=ib_physical_thems_7_2)
     await callback_query.answer()

@dp.callback_query_handler(text='18')
async def stolb2_physical_thems18(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_18, parse_mode='html',
                                   reply_markup=ib_physical_thems_8_2)
     await callback_query.answer()

@dp.callback_query_handler(text='19')
async def stolb2_physical_thems19(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_19, parse_mode='html',
                                   reply_markup=ib_physical_thems_9_2)
     await callback_query.answer()


@dp.callback_query_handler(text='20')
async def stolb2_physical_thems20(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_20, parse_mode='html',
                                   reply_markup=ib_physical_thems_10_2)
    await callback_query.answer()

@dp.callback_query_handler(text='21')
async def stolb3_physical_thems21(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_21, parse_mode='html',
                                   reply_markup=ib_physical_thems_1_3)
    await callback_query.answer()

@dp.callback_query_handler(text='22')
async def stolb3_physical_thems22(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_22,
                            reply_markup=ib_physical_thems_2_3)
     await callback_query.answer()

@dp.callback_query_handler(text='23')
async def stolb3_physical_thems23(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text = ph_t_23, parse_mode='html',
                                   reply_markup=ib_physical_thems_3_3)
    await callback_query.answer()

@dp.callback_query_handler(text='24')
async def stolb3_physical_thems24(callback_query : types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_24, parse_mode='html',
                                   reply_markup=ib_physical_thems_4_3)
    await callback_query.answer()

@dp.callback_query_handler(text='25')
async def stolb3_physical_thems25(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_25, parse_mode='html',
                                   reply_markup=ib_physical_thems_5_3)
     await callback_query.answer()

@dp.callback_query_handler(text='26')
async def stolb3_physical_thems26(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_26, parse_mode='html',
                                   reply_markup=ib_physical_thems_6_3)
     await callback_query.answer()

@dp.callback_query_handler(text='27')
async def stolb3_physical_thems27(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_27, parse_mode='html',
                                   reply_markup=ib_physical_thems_7_3)
     await callback_query.answer()

@dp.callback_query_handler(text='28')
async def stolb3_physical_thems28(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_28, parse_mode='html',
                                   reply_markup=ib_physical_thems_8_3)
     await callback_query.answer()

@dp.callback_query_handler(text='29')
async def stolb3_physical_thems29(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_29, parse_mode='html',
                                   reply_markup=ib_physical_thems_9_3)
     await callback_query.answer()

@dp.callback_query_handler(text='30')
async def stolb3_physical_thems30(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_30, parse_mode='html',
                                   reply_markup=ib_physical_thems_10_3)
     await callback_query.answer()


#возвращение в меню
@dp.callback_query_handler(text='back1')
async def stolb1_physical_thems_back1(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text='<b>Темы для проектов по физике</b>', parse_mode='html',
                                   reply_markup=ib_physical_thems)
     await callback_query.answer()


@dp.callback_query_handler(text='back2')
async def stolb2_physical_thems_back2(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text='<b>Темы для проектов по физике</b>', parse_mode='html',
                           reply_markup=ib_physical_thems)
    await callback_query.answer()

@dp.callback_query_handler(text='back3')
async def stolb3_physical_thems_back3(callback_query : types.CallbackQuery):
     await bot.send_message(chat_id=callback_query.from_user.id, text='<b>Темы для проектов по физике</b>', parse_mode='html',
                                   reply_markup=ib_physical_thems)
     await callback_query.answer()



#разделение на столбы
#а так же функции выбора тем
#1

@dp.callback_query_handler(text='q1')
async def physical_themes_1(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_1
    await bot.send_message(chat_id=callback_query.from_user.id, text= ph_t_1_2,reply_markup = ib_full_thems_1)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #   await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup = ib_full_thems_1)
    await callback_query.answer()





@dp.callback_query_handler(text='q2')
async def physical_themes_2(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_2
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_2_2,reply_markup = ib_full_thems_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q3')
async def physical_themes_3(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_3
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_3_2,reply_markup = ib_full_thems_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q4')
async def physical_themes_4(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_4
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_4_2,reply_markup = ib_full_thems_4)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_4)
    await callback_query.answer()

@dp.callback_query_handler(text='q5')
async def physical_themes_5(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_5
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_5_2,reply_markup = ib_full_thems_5)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_5)
    await callback_query.answer()

@dp.callback_query_handler(text='q6')
async def physical_themes_6(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_6
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_6_2,reply_markup = ib_full_thems_6)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_6)
    await callback_query.answer()

@dp.callback_query_handler(text='q7')
async def physical_themes_7(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_7
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_7_2,reply_markup = ib_full_thems_7)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_7)
    await callback_query.answer()

@dp.callback_query_handler(text='q8')
async def physical_themes_8(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_8
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_8_2,reply_markup = ib_full_thems_8)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_8)
    await callback_query.answer()

@dp.callback_query_handler(text='q9')
async def physical_themes_9(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_9
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_9_2,reply_markup = ib_full_thems_9)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_9)
    await callback_query.answer()

@dp.callback_query_handler(text='q10')
async def physical_themes_10(callback_query: types.CallbackQuery):
    global select_project
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_10_2,reply_markup = ib_full_thems_10)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_10)
    await callback_query.answer()
#2

@dp.callback_query_handler(text='q11')
async def physical_themes_11(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_11
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_11_2, reply_markup=ib_full_thems_1_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_1_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q12')
async def physical_themes_12(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_12
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_12_2, reply_markup=ib_full_thems_2_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_2_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q13')
async def physical_themes_13(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_13
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_13_2, reply_markup=ib_full_thems_3_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_3_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q14')
async def physical_themes_14(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_14
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_14_2, reply_markup=ib_full_thems_4_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_4_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q15')
async def physical_themes_15(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_15
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_15_2, reply_markup=ib_full_thems_5_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_5_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q16')
async def physical_themes_16(callback_query: types.CallbackQuery):
    global select_project
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_16_2, reply_markup=ib_full_thems_6_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_6_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q17')
async def physical_themes_17(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_17
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_17_2, reply_markup=ib_full_thems_7_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_7_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q18')
async def physical_themes_18(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_18
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_18_2, reply_markup=ib_full_thems_8_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_8_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q19')
async def physical_themes_19(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_19
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_19_2, reply_markup=ib_full_thems_9_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_9_2)
    await callback_query.answer()

@dp.callback_query_handler(text='q20')
async def physical_themes_20(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_20
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_20_2, reply_markup=ib_full_thems_10_2)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_10_2)
    await callback_query.answer()

#3

@dp.callback_query_handler(text='q21')
async def physical_themes_21(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_21
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_21_2, reply_markup=ib_full_thems_1_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_1_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q22')
async def physical_themes_22(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_22
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_22_2, reply_markup=ib_full_thems_2_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_2_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q23')
async def physical_themes_23(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_23
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_23_2, reply_markup=ib_full_thems_3_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_3_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q24')
async def physical_themes_24(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_24
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_24_2, reply_markup=ib_full_thems_4_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_4_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q25')
async def physical_themes_25(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_25
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_25_2, reply_markup=ib_full_thems_5_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_5_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q26')
async def physical_themes_26(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_26
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_26_2, reply_markup=ib_full_thems_6_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_6_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q27')
async def physical_themes_27(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_27
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_27_2, reply_markup=ib_full_thems_7_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_7_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q28')
async def physical_themes_28(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_28
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_28_2, reply_markup=ib_full_thems_8_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_8_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q29')
async def physical_themes_29(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_29
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_29_2, reply_markup=ib_full_thems_9_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_9_3)
    await callback_query.answer()

@dp.callback_query_handler(text='q30')
async def physical_themes_30(callback_query: types.CallbackQuery):
    global select_project
    select_project = ph_t_30
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_t_30_2, reply_markup=ib_full_thems_10_3)
    # with open("C:\School_Project_Bot\presentation.pdf", 'rb') as pdf1:
    #     await bot.send_document(chat_id=callback_query.from_user.id, document=pdf1, reply_markup=ib_full_thems_10_3)
    await callback_query.answer()


#выход к меню с темами
@dp.callback_query_handler(text='backq1')
async def back_physical_themes_1(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_sp_1,
                           reply_markup= ib_stolb1_physical_thems)
    await callback_query.answer()


@dp.callback_query_handler(text='backq2')
async def back_physical_themes_2(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_sp_2,
                           reply_markup= ib_stolb2_physical_thems)
    await callback_query.answer()


@dp.callback_query_handler(text='backq3')
async def back_physical_themes_3(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text=ph_sp_3,
                           reply_markup= ib_stolb3_physical_thems)
    await callback_query.answer()


#передача темы в меню
#
# @dp.message_handler(lambda message : 'Мой проект' in message.text)
# async def my_project(message : types.Message):
#     await message.answer('Ваш проект', reply_markup= kb_my_project )
#
# @dp.message_handler(lambda message : 'Проект' in message.text)
# async def project(message : types.Message):
#     global select_project
#     if select_project:
#         await message.answer('Ваш проект:\n'+select_project, reply_markup= kb_my_project)
#     else:
#         await message.answer('Вы еще не определились с проектом', reply_markup= kb_my_project)
#
# @dp.message_handler(lambda message : 'Удалить выбранный проект' in message.text)
# async def delete_project(message : types.Message):
#     global select_project
#     select_project = None
#     await message.answer('Выбранная тема удалена', reply_markup=kb_my_project)
