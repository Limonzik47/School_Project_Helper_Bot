from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#список
ib_physical_thems = InlineKeyboardMarkup(row_width=3)
b_physical_themes1 = InlineKeyboardButton(text='Список 1',callback_data='a1')
b_physical_themes2 = InlineKeyboardButton(text='Список 2',callback_data='a2')
b_physical_themes3 = InlineKeyboardButton(text='Список 3',callback_data='a3')
b_physical_themes4 = InlineKeyboardButton(text='Назад',callback_data='backa4')
ib_physical_thems.row(b_physical_themes1,b_physical_themes2,b_physical_themes3).add(b_physical_themes4)

#1.0
ib_stolb1_physical_thems = InlineKeyboardMarkup(row_width=2)
b_stolb1_physical_thems1 = InlineKeyboardButton(text='1', callback_data= '1')
b_stolb1_physical_thems2 = InlineKeyboardButton(text='2', callback_data= '2')
b_stolb1_physical_thems3 = InlineKeyboardButton(text='3', callback_data= '3')
b_stolb1_physical_thems4 = InlineKeyboardButton(text='4', callback_data= '4')
b_stolb1_physical_thems5 = InlineKeyboardButton(text='5', callback_data= '5')
b_stolb1_physical_thems6 = InlineKeyboardButton(text='6', callback_data= '6')
b_stolb1_physical_thems7 = InlineKeyboardButton(text='7', callback_data= '7')
b_stolb1_physical_thems8 = InlineKeyboardButton(text='8', callback_data= '8')
b_stolb1_physical_thems9 = InlineKeyboardButton(text='9', callback_data= '9')
b_stolb1_physical_thems10 = InlineKeyboardButton(text='10', callback_data= '10')
b_stolb1_physical_thems11 = InlineKeyboardButton(text='Назад', callback_data='back1')
b_stolb1_physical_thems12 =InlineKeyboardButton(text='Следующий', callback_data='continie1')
ib_stolb1_physical_thems.row(b_stolb1_physical_thems1,
                             b_stolb1_physical_thems2).row(b_stolb1_physical_thems3,
                                                           b_stolb1_physical_thems4).row(b_stolb1_physical_thems5,
                                                                                         b_stolb1_physical_thems6).row(b_stolb1_physical_thems7,
                                                                                                                       b_stolb1_physical_thems8).row(b_stolb1_physical_thems9,
                                                                                                                                                     b_stolb1_physical_thems10).add(b_stolb1_physical_thems12).add(b_stolb1_physical_thems11)
#1.1
ib_physical_thems_1 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_1 = InlineKeyboardButton(text='Посмотреть', callback_data='q1')
b_physical_thems_2_1 = InlineKeyboardButton(text='Вернуться к темам', callback_data='backq1')
ib_physical_thems_1.row(b_physical_thems_1_1,b_physical_thems_2_1)

ib_physical_thems_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q2')
ib_physical_thems_2.row(b_physical_thems_1_2,b_physical_thems_2_1)

ib_physical_thems_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q3')
ib_physical_thems_3.row(b_physical_thems_1_3,b_physical_thems_2_1)

ib_physical_thems_4 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_4 = InlineKeyboardButton(text='Посмотреть', callback_data='q4')
ib_physical_thems_4.row(b_physical_thems_1_4,b_physical_thems_2_1)

ib_physical_thems_5 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_5 = InlineKeyboardButton(text='Посмотреть', callback_data='q5')
ib_physical_thems_5.row(b_physical_thems_1_5,b_physical_thems_2_1)

ib_physical_thems_6 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_6 = InlineKeyboardButton(text='Посмотреть', callback_data='q6')
ib_physical_thems_6.row(b_physical_thems_1_6,b_physical_thems_2_1)

ib_physical_thems_7 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_7 = InlineKeyboardButton(text='Посмотреть', callback_data='q7')
ib_physical_thems_7.row(b_physical_thems_1_7,b_physical_thems_2_1)

ib_physical_thems_8 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_8 = InlineKeyboardButton(text='Посмотреть', callback_data='q8')
ib_physical_thems_8.row(b_physical_thems_1_8,b_physical_thems_2_1)

ib_physical_thems_9 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_9 = InlineKeyboardButton(text='Посмотреть', callback_data='q9')
ib_physical_thems_9.row(b_physical_thems_1_9,b_physical_thems_2_1)

ib_physical_thems_10 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_10 = InlineKeyboardButton(text='Посмотреть', callback_data='q10')
ib_physical_thems_10.row(b_physical_thems_1_10,b_physical_thems_2_1)

#1.2
ib_full_thems_1 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_1.row(b_physical_thems_2_1)

ib_full_thems_2 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_2.row(b_physical_thems_2_1)

ib_full_thems_3 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_3.row(b_physical_thems_2_1)

ib_full_thems_4 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_4.row(b_physical_thems_2_1)

ib_full_thems_5 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_5.row(b_physical_thems_2_1)

ib_full_thems_6 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_6.row(b_physical_thems_2_1)

ib_full_thems_7 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_7.row(b_physical_thems_2_1)

ib_full_thems_8 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_8.row(b_physical_thems_2_1)

ib_full_thems_9 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_9.row(b_physical_thems_2_1)

ib_full_thems_10 = InlineKeyboardMarkup(row_width=1)
ib_full_thems_10.row(b_physical_thems_2_1)



#2.0
ib_stolb2_physical_thems = InlineKeyboardMarkup(row_width=2)
b_stolb2_physical_thems1 = InlineKeyboardButton(text='11', callback_data= '11')
b_stolb2_physical_thems2 = InlineKeyboardButton(text='12', callback_data= '12')
b_stolb2_physical_thems3 = InlineKeyboardButton(text='13', callback_data= '13')
b_stolb2_physical_thems4 = InlineKeyboardButton(text='14', callback_data= '14')
b_stolb2_physical_thems5 = InlineKeyboardButton(text='15', callback_data= '15')
b_stolb2_physical_thems6 = InlineKeyboardButton(text='16', callback_data= '16')
b_stolb2_physical_thems7 = InlineKeyboardButton(text='17', callback_data= '17')
b_stolb2_physical_thems8 = InlineKeyboardButton(text='18', callback_data= '18')
b_stolb2_physical_thems9 = InlineKeyboardButton(text='19', callback_data= '19')
b_stolb2_physical_thems10 = InlineKeyboardButton(text='20', callback_data= '20')
b_stolb2_physical_thems11 = InlineKeyboardButton(text='Назад', callback_data='back2')
b_stolb2_physical_thems12 = InlineKeyboardButton(text='Следующий', callback_data='continie2')
ib_stolb2_physical_thems.row(b_stolb2_physical_thems1,
                             b_stolb2_physical_thems2).row(b_stolb2_physical_thems3,
                                                           b_stolb2_physical_thems4).row(b_stolb2_physical_thems5,
                                                                                         b_stolb2_physical_thems6).row(b_stolb2_physical_thems7,
                                                                                                                       b_stolb2_physical_thems8).row(b_stolb2_physical_thems9,
                                                                                                                                                     b_stolb2_physical_thems10).add(b_stolb2_physical_thems12).add(b_stolb2_physical_thems11)

#2.1
ib_physical_thems_1_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_1_1 = InlineKeyboardButton(text='Посмотреть', callback_data='q11')
b_physical_thems_1_0_1 = InlineKeyboardButton(text='Вернуться к темам', callback_data='backq2')
ib_physical_thems_1_2.row(b_physical_thems_1_1_1,b_physical_thems_1_0_1)

ib_physical_thems_2_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_2_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q12')
ib_physical_thems_2_2.row(b_physical_thems_1_2_2,b_physical_thems_1_0_1)

ib_physical_thems_3_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_3_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q13')
ib_physical_thems_3_2.row(b_physical_thems_1_3_2,b_physical_thems_1_0_1)

ib_physical_thems_4_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_4_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q14')
ib_physical_thems_4_2.row(b_physical_thems_1_4_2,b_physical_thems_1_0_1)

ib_physical_thems_5_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_5_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q15')
ib_physical_thems_5_2.row(b_physical_thems_1_5_2,b_physical_thems_1_0_1)

ib_physical_thems_6_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_6_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q16')
ib_physical_thems_6_2.row(b_physical_thems_1_6_2,b_physical_thems_1_0_1)

ib_physical_thems_7_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_7_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q17')
ib_physical_thems_7_2.row(b_physical_thems_1_7_2,b_physical_thems_1_0_1)

ib_physical_thems_8_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_8_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q18')
ib_physical_thems_8_2.row(b_physical_thems_1_8_2,b_physical_thems_1_0_1)

ib_physical_thems_9_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_9_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q19')
ib_physical_thems_9_2.row(b_physical_thems_1_9_2,b_physical_thems_1_0_1)

ib_physical_thems_10_2 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_10_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q20')
ib_physical_thems_10_2.row(b_physical_thems_1_10_2,b_physical_thems_1_0_1)

#2.2
ib_full_thems_1_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_1_2.row(b_physical_thems_1_0_1)

ib_full_thems_2_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_2_2.row(b_physical_thems_1_0_1)

ib_full_thems_3_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_3_2.row(b_physical_thems_1_0_1)

ib_full_thems_3_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_3_2.row(b_physical_thems_1_0_1)

ib_full_thems_4_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_4_2.row(b_physical_thems_1_0_1)

ib_full_thems_5_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_5_2.row(b_physical_thems_1_0_1)

ib_full_thems_6_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_6_2.row(b_physical_thems_1_0_1)

ib_full_thems_7_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_7_2.row(b_physical_thems_1_0_1)

ib_full_thems_8_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_8_2.row(b_physical_thems_1_0_1)

ib_full_thems_9_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_9_2.row(b_physical_thems_1_0_1)

ib_full_thems_10_2 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_10_2.row(b_physical_thems_1_0_1)

#3.0
ib_stolb3_physical_thems = InlineKeyboardMarkup(row_width=2)
b_stolb3_physical_thems1 = InlineKeyboardButton(text='21', callback_data= '21')
b_stolb3_physical_thems2 = InlineKeyboardButton(text='22', callback_data= '22')
b_stolb3_physical_thems3 = InlineKeyboardButton(text='23', callback_data= '23')
b_stolb3_physical_thems4 = InlineKeyboardButton(text='24', callback_data= '24')
b_stolb3_physical_thems5 = InlineKeyboardButton(text='25', callback_data= '25')
b_stolb3_physical_thems6 = InlineKeyboardButton(text='26', callback_data= '26')
b_stolb3_physical_thems7 = InlineKeyboardButton(text='27', callback_data= '27')
b_stolb3_physical_thems8 = InlineKeyboardButton(text='28', callback_data= '28')
b_stolb3_physical_thems9 = InlineKeyboardButton(text='29', callback_data= '29')
b_stolb3_physical_thems10 = InlineKeyboardButton(text='30', callback_data= '30')
b_stolb3_physical_thems11 = InlineKeyboardButton(text='Назад', callback_data='back3')

ib_stolb3_physical_thems.row(b_stolb3_physical_thems1,
                             b_stolb3_physical_thems2).row(b_stolb3_physical_thems3,
                                                           b_stolb3_physical_thems4).row(b_stolb3_physical_thems5,
                                                                                         b_stolb3_physical_thems6).row(b_stolb3_physical_thems7,
                                                                                                                       b_stolb3_physical_thems8).row(b_stolb3_physical_thems9,
                                                                                                                                                     b_stolb3_physical_thems10).add(b_stolb3_physical_thems11)
#3.1
ib_physical_thems_1_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_1_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q21')
b_physical_thems_3_3_3 = InlineKeyboardButton(text='Вернуться к темам', callback_data='backq3')
ib_physical_thems_1_3.row(b_physical_thems_1_1_3,b_physical_thems_3_3_3)

ib_physical_thems_2_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_2_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q22')
ib_physical_thems_2_3.row(b_physical_thems_1_2_3,b_physical_thems_3_3_3)

ib_physical_thems_3_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_3_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q23')
ib_physical_thems_3_3.row(b_physical_thems_1_3_3,b_physical_thems_3_3_3)

ib_physical_thems_4_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_4_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q24')
ib_physical_thems_4_3.row(b_physical_thems_1_4_3,b_physical_thems_3_3_3)

ib_physical_thems_5_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_5_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q25')
ib_physical_thems_5_3.row(b_physical_thems_1_5_3,b_physical_thems_3_3_3)

ib_physical_thems_6_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_6_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q26')
ib_physical_thems_6_3.row(b_physical_thems_1_6_3,b_physical_thems_3_3_3)

ib_physical_thems_7_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_7_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q27')
ib_physical_thems_7_3.row(b_physical_thems_1_7_3,b_physical_thems_3_3_3)

ib_physical_thems_8_3= InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_8_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q28')
ib_physical_thems_8_3.row(b_physical_thems_1_8_3,b_physical_thems_3_3_3)

ib_physical_thems_9_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_9_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q29')
ib_physical_thems_9_3.row(b_physical_thems_1_9_3,b_physical_thems_3_3_3)

ib_physical_thems_10_3 = InlineKeyboardMarkup(row_width=2)
b_physical_thems_1_10_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q30')
ib_physical_thems_10_3.row(b_physical_thems_1_10_3,b_physical_thems_3_3_3)

#3.2
ib_full_thems_1_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_1_3.row(b_physical_thems_3_3_3)

ib_full_thems_2_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_2_3.row(b_physical_thems_3_3_3)

ib_full_thems_3_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_3_3.row(b_physical_thems_3_3_3)

ib_full_thems_4_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_4_3.row(b_physical_thems_3_3_3)

ib_full_thems_5_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_5_3.row(b_physical_thems_3_3_3)

ib_full_thems_6_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_6_3.row(b_physical_thems_3_3_3)

ib_full_thems_7_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_7_3.row(b_physical_thems_3_3_3)

ib_full_thems_8_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_8_3.row(b_physical_thems_3_3_3)

ib_full_thems_9_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_9_3.row(b_physical_thems_3_3_3)

ib_full_thems_10_3 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_10_3.row(b_physical_thems_3_3_3)


