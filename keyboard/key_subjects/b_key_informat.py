from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#список
ib_informatika_thems = InlineKeyboardMarkup(row_width=2)
b_informatika_thems1 = InlineKeyboardButton(text='Список 1', callback_data='a5')
b_informatika_thems2 = InlineKeyboardButton(text='Список 2', callback_data='a6')
b_informatika_thems3 = InlineKeyboardButton(text='Список 3', callback_data='a7')
b_informatika_thems4 = InlineKeyboardButton(text='Назад', callback_data='backa8')
ib_informatika_thems.row(b_informatika_thems1,b_informatika_thems2,b_informatika_thems3).add(b_informatika_thems4)

#1.0
ib_stolb1_informatika_thems = InlineKeyboardMarkup(row_width=2)
b_stolb1_informatika_thems1 = InlineKeyboardButton(text='1', callback_data='31')
b_stolb1_informatika_thems2 = InlineKeyboardButton(text='2', callback_data='32')
b_stolb1_informatika_thems3 = InlineKeyboardButton(text='3', callback_data='33')
b_stolb1_informatika_thems4 = InlineKeyboardButton(text='4', callback_data='34')
b_stolb1_informatika_thems5 = InlineKeyboardButton(text='5', callback_data='35')
b_stolb1_informatika_thems6 = InlineKeyboardButton(text='6', callback_data='36')
b_stolb1_informatika_thems7 = InlineKeyboardButton(text='7', callback_data='37')
b_stolb1_informatika_thems8 = InlineKeyboardButton(text='8', callback_data='38')
b_stolb1_informatika_thems9 = InlineKeyboardButton(text='9', callback_data='39')
b_stolb1_informatika_thems10 = InlineKeyboardButton(text='10', callback_data='40')
b_stolb1_informatika_thems11= InlineKeyboardButton(text='Назад', callback_data='back4')
b_stolb1_informatika_thems12 = InlineKeyboardButton(text='Следующий', callback_data='continie3')
ib_stolb1_informatika_thems.row(b_stolb1_informatika_thems1,
                                b_stolb1_informatika_thems2).row(b_stolb1_informatika_thems3,
                                                                 b_stolb1_informatika_thems4).row(b_stolb1_informatika_thems5,
                                                                                                  b_stolb1_informatika_thems6).row(b_stolb1_informatika_thems7,
                                                                                                                                   b_stolb1_informatika_thems8).row(b_stolb1_informatika_thems9,
                                                                                                                                                                    b_stolb1_informatika_thems10).add(b_stolb1_informatika_thems12).add(b_stolb1_informatika_thems11)

#1.1
ib_informatika_thems_1 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q31')
b_informatika_thems_1_2 = InlineKeyboardButton(text='Вернуться к темам', callback_data='backq4')
ib_informatika_thems_1.row(b_informatika_thems_1_1,b_informatika_thems_1_2)

ib_informatika_thems_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_2_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q32')
ib_informatika_thems_2.row(b_informatika_thems_2_1,b_informatika_thems_1_2)

ib_informatika_thems_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_3_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q33')
ib_informatika_thems_3.row(b_informatika_thems_3_1,b_informatika_thems_1_2)

ib_informatika_thems_4 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_4_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q34')
ib_informatika_thems_4.row(b_informatika_thems_4_1,b_informatika_thems_1_2)

ib_informatika_thems_5 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_5_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q35')
ib_informatika_thems_5.row(b_informatika_thems_5_1,b_informatika_thems_1_2)

ib_informatika_thems_6 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_6_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q36')
ib_informatika_thems_6.row(b_informatika_thems_6_1,b_informatika_thems_1_2)

ib_informatika_thems_7 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_7_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q37')
ib_informatika_thems_7.row(b_informatika_thems_7_1,b_informatika_thems_1_2)


ib_informatika_thems_8 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_8_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q38')
ib_informatika_thems_8.row(b_informatika_thems_8_1,b_informatika_thems_1_2)


ib_informatika_thems_9 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_9_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q39')
ib_informatika_thems_9.row(b_informatika_thems_9_1,b_informatika_thems_1_2)


ib_informatika_thems_10 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_10_1 = InlineKeyboardButton(text = 'Посмотреть', callback_data='q40')
ib_informatika_thems_10.row(b_informatika_thems_10_1,b_informatika_thems_1_2)


#1.2
ib_full_thems_1_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_1_4.row(b_informatika_thems_1_2)

ib_full_thems_2_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_2_4.row(b_informatika_thems_1_2)

ib_full_thems_3_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_3_4.row(b_informatika_thems_1_2)

ib_full_thems_4_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_4_4.row(b_informatika_thems_1_2)

ib_full_thems_5_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_5_4.row(b_informatika_thems_1_2)

ib_full_thems_6_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_6_4.row(b_informatika_thems_1_2)

ib_full_thems_7_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_7_4.row(b_informatika_thems_1_2)

ib_full_thems_8_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_8_4.row(b_informatika_thems_1_2)

ib_full_thems_9_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_9_4.row(b_informatika_thems_1_2)

ib_full_thems_10_4 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_10_4.row(b_informatika_thems_1_2)

#2.0
ib_stolb2_informatika_thems = InlineKeyboardMarkup(row_width=2)
b_stolb2_informatika_thems1 = InlineKeyboardButton(text='11', callback_data='41')
b_stolb2_informatika_thems2 = InlineKeyboardButton(text='12', callback_data='42')
b_stolb2_informatika_thems3 = InlineKeyboardButton(text='13', callback_data='43')
b_stolb2_informatika_thems4 = InlineKeyboardButton(text='14', callback_data='44')
b_stolb2_informatika_thems5 = InlineKeyboardButton(text='15', callback_data='45')
b_stolb2_informatika_thems6 = InlineKeyboardButton(text='16', callback_data='46')
b_stolb2_informatika_thems7 = InlineKeyboardButton(text='17', callback_data='47')
b_stolb2_informatika_thems8 = InlineKeyboardButton(text='18', callback_data='48')
b_stolb2_informatika_thems9 = InlineKeyboardButton(text='19', callback_data='49')
b_stolb2_informatika_thems10 = InlineKeyboardButton(text='20', callback_data='50')
b_stolb2_informatika_thems11 = InlineKeyboardButton(text='Назад', callback_data='back5')
b_stolb2_informatika_thems12 = InlineKeyboardButton(text='Следующий', callback_data='continie4')
ib_stolb2_informatika_thems.row(b_stolb2_informatika_thems1,
                                b_stolb2_informatika_thems2).row(b_stolb2_informatika_thems3,
                                                                 b_stolb2_informatika_thems4).row(b_stolb2_informatika_thems5,
                                                                                                  b_stolb2_informatika_thems6).row(b_stolb2_informatika_thems7,
                                                                                                                                   b_stolb2_informatika_thems8).row(b_stolb2_informatika_thems9,
                                                                                                                                                                    b_stolb2_informatika_thems10).add(b_stolb2_informatika_thems12).add(b_stolb2_informatika_thems11)

#2.1
ib_informatika_thems_1_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_1_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q41')
b_informatika_thems_1_11_2 = InlineKeyboardButton(text='Вернуться к темам', callback_data='backq5')
ib_informatika_thems_1_2.row(b_informatika_thems_1_1_2, b_informatika_thems_1_11_2)

ib_informatika_thems_2_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_2_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q42')
ib_informatika_thems_2_2.row(b_informatika_thems_1_2_2, b_informatika_thems_1_11_2)

ib_informatika_thems_3_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_3_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q43')
ib_informatika_thems_3_2.row(b_informatika_thems_1_3_2, b_informatika_thems_1_11_2)

ib_informatika_thems_4_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_4_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q44')
ib_informatika_thems_4_2.row(b_informatika_thems_1_4_2, b_informatika_thems_1_11_2)

ib_informatika_thems_5_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_5_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q45')
ib_informatika_thems_5_2.row(b_informatika_thems_1_5_2, b_informatika_thems_1_11_2)

ib_informatika_thems_6_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_6_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q46')
ib_informatika_thems_6_2.row(b_informatika_thems_1_6_2, b_informatika_thems_1_11_2)

ib_informatika_thems_7_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_7_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q47')
ib_informatika_thems_7_2.row(b_informatika_thems_1_7_2, b_informatika_thems_1_11_2)

ib_informatika_thems_8_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_8_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q48')
ib_informatika_thems_8_2.row(b_informatika_thems_1_8_2, b_informatika_thems_1_11_2)

ib_informatika_thems_9_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_9_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q49')
ib_informatika_thems_9_2.row(b_informatika_thems_1_9_2, b_informatika_thems_1_11_2)

ib_informatika_thems_10_2 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_10_2 = InlineKeyboardButton(text='Посмотреть', callback_data='q50')
ib_informatika_thems_10_2.row(b_informatika_thems_1_10_2, b_informatika_thems_1_11_2)

#2.2
ib_full_thems_1_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_1_5.row(b_informatika_thems_1_11_2)

ib_full_thems_2_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_2_5.row(b_informatika_thems_1_11_2)

ib_full_thems_3_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_3_5.row(b_informatika_thems_1_11_2)

ib_full_thems_4_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_4_5.row(b_informatika_thems_1_11_2)

ib_full_thems_5_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_5_5.row(b_informatika_thems_1_11_2)

ib_full_thems_6_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_6_5.row(b_informatika_thems_1_11_2)

ib_full_thems_7_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_7_5.row(b_informatika_thems_1_11_2)

ib_full_thems_8_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_8_5.row(b_informatika_thems_1_11_2)

ib_full_thems_9_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_9_5.row(b_informatika_thems_1_11_2)

ib_full_thems_10_5 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_10_5.row(b_informatika_thems_1_11_2)

#3.0
ib_stolb3_informatika_thems = InlineKeyboardMarkup(row_width=2)
b_stolb3_informatika_thems1 = InlineKeyboardButton(text='21', callback_data='51')
b_stolb3_informatika_thems2 = InlineKeyboardButton(text='22', callback_data='52')
b_stolb3_informatika_thems3 = InlineKeyboardButton(text='23', callback_data='53')
b_stolb3_informatika_thems4 = InlineKeyboardButton(text='24', callback_data='54')
b_stolb3_informatika_thems5 = InlineKeyboardButton(text='25', callback_data='55')
b_stolb3_informatika_thems6 = InlineKeyboardButton(text='26', callback_data='56')
b_stolb3_informatika_thems7 = InlineKeyboardButton(text='27', callback_data='57')
b_stolb3_informatika_thems8 = InlineKeyboardButton(text='28', callback_data='58')
b_stolb3_informatika_thems9 = InlineKeyboardButton(text='29', callback_data='59')
b_stolb3_informatika_thems10 = InlineKeyboardButton(text='30', callback_data='60')
b_stolb3_informatika_thems11 = InlineKeyboardButton(text='Назад', callback_data='back6')
ib_stolb3_informatika_thems.row(b_stolb3_informatika_thems1,
                                b_stolb3_informatika_thems2).row( b_stolb3_informatika_thems3,
                                                                  b_stolb3_informatika_thems4).row(b_stolb3_informatika_thems5,
                                                                                                   b_stolb3_informatika_thems6).row(b_stolb3_informatika_thems7,
                                                                                                                                    b_stolb3_informatika_thems8).row(b_stolb3_informatika_thems9, b_stolb3_informatika_thems10).add(b_stolb3_informatika_thems11)

#3.1
ib_informatika_thems_1_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_1_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q51')
b_informatika_thems_1_13_3 = InlineKeyboardButton(text='Вернуться к темам', callback_data='backq6')
ib_informatika_thems_1_3.row(b_informatika_thems_1_1_3, b_informatika_thems_1_13_3)

ib_informatika_thems_2_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_2_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q52')
ib_informatika_thems_2_3.row(b_informatika_thems_1_2_3, b_informatika_thems_1_13_3)

ib_informatika_thems_3_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_3_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q53')
ib_informatika_thems_3_3.row(b_informatika_thems_1_3_3, b_informatika_thems_1_13_3)

ib_informatika_thems_4_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_4_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q54')
ib_informatika_thems_4_3.row(b_informatika_thems_1_4_3, b_informatika_thems_1_13_3)

ib_informatika_thems_5_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_5_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q55')
ib_informatika_thems_5_3.row(b_informatika_thems_1_5_3, b_informatika_thems_1_13_3)

ib_informatika_thems_6_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_6_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q56')
ib_informatika_thems_6_3.row(b_informatika_thems_1_6_3, b_informatika_thems_1_13_3)

ib_informatika_thems_7_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_7_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q57')
ib_informatika_thems_7_3.row(b_informatika_thems_1_7_3, b_informatika_thems_1_13_3)

ib_informatika_thems_8_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_8_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q58')
ib_informatika_thems_8_3.row(b_informatika_thems_1_8_3, b_informatika_thems_1_13_3)

ib_informatika_thems_9_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_9_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q59')
ib_informatika_thems_9_3.row(b_informatika_thems_1_8_3, b_informatika_thems_1_13_3)

ib_informatika_thems_10_3 = InlineKeyboardMarkup(row_width=2)
b_informatika_thems_1_10_3 = InlineKeyboardButton(text='Посмотреть', callback_data='q60')
ib_informatika_thems_10_3.row(b_informatika_thems_1_10_3, b_informatika_thems_1_13_3)

#3.2

ib_full_thems_1_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_1_6.row(b_informatika_thems_1_13_3)

ib_full_thems_2_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_2_6.row(b_informatika_thems_1_13_3)

ib_full_thems_3_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_3_6.row(b_informatika_thems_1_13_3)

ib_full_thems_4_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_4_6.row(b_informatika_thems_1_13_3)

ib_full_thems_5_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_5_6.row(b_informatika_thems_1_13_3)

ib_full_thems_6_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_6_6.row(b_informatika_thems_1_13_3)

ib_full_thems_7_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_7_6.row(b_informatika_thems_1_13_3)

ib_full_thems_8_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_8_6.row(b_informatika_thems_1_13_3)

ib_full_thems_9_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_9_6.row(b_informatika_thems_1_13_3)

ib_full_thems_10_6 = InlineKeyboardMarkup(row_width=2)
ib_full_thems_10_6.row(b_informatika_thems_1_13_3)





