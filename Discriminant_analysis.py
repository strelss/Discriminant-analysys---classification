import PySimpleGUI as sg
import numpy as np
import math
from discrim_module import average_vectors as vec
from discrim_module import covar_matrix as cov_mat
from discrim_module import decision_making as dec_mak
from discrim_module import diagnostic_assessment as  dia_as

col_obj1 = [
    [sg.Text('', size=(23, 1)), sg.Text('Образ S\u00b9', size=(10, 1), font=("Helvetica", 15))],
    [sg.Text('', size=(9, 1)), sg.Text('Объект obj₁', size=(10, 1), font=("Helvetica", 11)), sg.Text('Объект obj₂', size=(10, 1), font=("Helvetica", 11)),
     sg.Text('Объект obj₃', size=(10, 1), font=("Helvetica", 11)), sg.Text('Объект obj₄', size=(10, 1), font=("Helvetica", 11)), ],
    [sg.Text('Признак x₁', font=("Helvetica", 11)), sg.Input('31.33', size=(11, 1), key='s1X1x1', font=("Helvetica", 11)),
     sg.Input('32.78', size=(11, 1), key='s1X2x1', font=("Helvetica", 11)), sg.Input('35.61', size=(11, 1), key='s1X3x1', font=("Helvetica", 11)), sg.Input('30.54', size=(11, 1), key='s1X4x1', font=("Helvetica", 11)), ],
    [sg.Text('Признак x₂', font=("Helvetica", 11)), sg.Input('4.15', size=(11, 1), key='s1X1x2', font=("Helvetica", 11)),
     sg.Input('3.34', size=(11, 1), key='s1X2x2', font=("Helvetica", 11)), sg.Input('5.56', size=(11, 1), key='s1X3x2', font=("Helvetica", 11)), sg.Input('4.76', size=(11, 1), key='s1X4x2', font=("Helvetica", 11)), ],
    [sg.Text('Признак x₃', font=("Helvetica", 11)), sg.Input('79', size=(11, 1), key='s1X1x3', font=("Helvetica", 11)), sg.Input('81', size=(11, 1), key='s1X2x3', font=("Helvetica", 11)),
     sg.Input('82', size=(11, 1), key='s1X3x3', font=("Helvetica", 11)), sg.Input('80', size=(11, 1), key='s1X4x3', font=("Helvetica", 11)), ],
]

col_obj2 = [
    [sg.Text('', size=(23, 1)), sg.Text('Образ S\u00b2', size=(10, 1), font=("Helvetica", 15))],
    [sg.Text('', size=(9, 1)), sg.Text('Объект obj₁', size=(10, 1), font=("Helvetica", 11)), sg.Text('Объект obj₂', size=(10, 1), font=("Helvetica", 11)),
     sg.Text('Объект obj₃', size=(10, 1), font=("Helvetica", 11)), sg.Text('Объект obj₄', size=(10, 1), font=("Helvetica", 11)), sg.Text('Объект obj₅', size=(10, 1), font=("Helvetica", 11)), ],
    [sg.Text('Признак x₁', font=("Helvetica", 11)), sg.Input('12.25', size=(11, 1), key='s2X1x1', font=("Helvetica", 11)),
     sg.Input('13.09', size=(11, 1), key='s2X2x1', font=("Helvetica", 11)), sg.Input('7.65', size=(11, 1), key='s2X3x1', font=("Helvetica", 11)), sg.Input('9.98', size=(11, 1), key='s2X4x1', font=("Helvetica", 11)), sg.Input('8.77', size=(11, 1), key='s2X5x1', font=("Helvetica", 11)), ],
    [sg.Text('Признак x₂', font=("Helvetica", 11)), sg.Input('2.98', size=(11, 1), key='s2X1x2', font=("Helvetica", 11)),
     sg.Input('3.01', size=(11, 1), key='s2X2x2', font=("Helvetica", 11)), sg.Input('2.38', size=(11, 1), key='s2X3x2', font=("Helvetica", 11)),  sg.Input('2.73', size=(11, 1), key='s2X4x2', font=("Helvetica", 11)),  sg.Input('2.91', size=(11, 1), key='s2X5x2', font=("Helvetica", 11)), ],
    [sg.Text('Признак x₃', font=("Helvetica", 11)), sg.Input('66', size=(11, 1), key='s2X1x3', font=("Helvetica", 11)), sg.Input('69', size=(11, 1), key='s2X2x3', font=("Helvetica", 11)),
     sg.Input('58', size=(11, 1), key='s2X3x3', font=("Helvetica", 11)), sg.Input('71', size=(11, 1), key='s2X4x3', font=("Helvetica", 11)), sg.Input('55', size=(11, 1), key='s2X5x3', font=("Helvetica", 11)), ],
    [sg.Text('', size=(1, 2))]
]

research_obj = [
    [sg.Text('', size=(1, 1))],
    [sg.Text('Исследуемый объект \u1E8C', size=(20, 1), font=("Helvetica", 12))],
    [sg.Text('Признак x₁', font=("Helvetica", 11)), sg.Input('33.21', size=(11, 1), key='s3x1', font=("Helvetica", 11))],
    [sg.Text('Признак x₂', font=("Helvetica", 11)), sg.Input('5.58', size=(11, 1), key='s3x2', font=("Helvetica", 11))],
    [sg.Text('Признак x₃', font=("Helvetica", 11)), sg.Input('79', size=(11, 1), key='s3x3', font=("Helvetica", 11))],
]

layout = [
    [sg.Column(col_obj1), sg.Column(research_obj)],
    [sg.Column(col_obj2)],
    [sg.Output(size=(102, 20))],
    [sg.Submit('Начать исследование'), sg.Submit('Справка'), sg.Cancel('Выход')]
]
window = sg.Window('Discriminant_classification', layout)


sg.popup('Запущена программа дискриминантного анализа - классификации объектов.\n'
         'Подробная информация содержится в справке.\n'
         '\n'
         'dndia v.1.0')


while True:  # The Event Loop
    event, values = window.read()

    if event in (None, 'Выход', 'Cancel'):
        break
    if event == 'Начать исследование':


        print('Начало расчета:')
        print()

                    #Взятие введенных данных и упаковка в кортежи
        evid_s1 = (float(values['s1X1x1']), float(values['s1X2x1']), float(values['s1X3x1']), float(values['s1X4x1']),
                   float(values['s1X1x2']), float(values['s1X2x2']), float(values['s1X3x2']), float(values['s1X4x2']),
                   float(values['s1X1x3']), float(values['s1X2x3']), float(values['s1X3x3']), float(values['s1X4x3']))

        evid_s2 = (float(values['s2X1x1']), float(values['s2X2x1']), float(values['s2X3x1']), float(values['s2X4x1']), float(values['s2X5x1']),
                   float(values['s2X1x2']), float(values['s2X2x2']), float(values['s2X3x2']), float(values['s2X4x2']), float(values['s2X5x2']),
                   float(values['s2X1x3']), float(values['s2X2x3']), float(values['s2X3x3']), float(values['s2X4x3']), float(values['s2X5x3']))

        evid_s3 = (float(values['s3x1']), float(values['s3x2']), float(values['s3x3']))

        print('Введенные данные:')
        print()
        print('1. Образ Образ S\u00b9: ' + str(evid_s1))
        print()
        print('2. Образ Образ S\u00b2: ' + str(evid_s2))
        print()
        print('3. Исследуемый объект \u1E8C: ' + str(evid_s3))
        print('______________________________________________________________________________________________')
        print()

        def main():
            first_module = vec.Middle_Vektor(4, 3, 5, 3, evid_s1, evid_s2)
            first_module = first_module.give()

            first_module_part_2 = cov_mat.Kovar_Matrix(first_module[2], first_module[3], first_module[4], first_module[5], first_module[6], first_module[7], evid_s1, evid_s2, 4, 3, 5, 3)
            first_module_part_2 = first_module_part_2.inverse_covariance_matrix()

            second_module = dec_mak.Decision_making(first_module[0], first_module[1], first_module_part_2, 1, evid_s3)
            second_module = second_module.decision()

            third_module = dia_as.Diagnostic_assessment(first_module[0], first_module[1], first_module_part_2, 4, 5, 1)
            third_module = third_module.main()

            print()
            print('В результате вычислений сделан такой вывод: ')
            if second_module[1] == 1:
                print()
                print('        исследуемый объект \u1E8C принадлежит к образу S\u00b9 с вероятностью ' + str(third_module))
            elif second_module[1] == 2:
                print()
                print('        исследуемый объект \u1E8C принадлежит к образу S\u00b2 с вероятностью ' + str(third_module))
            print()
            print('Исследование завершено.')
        main()

    if event == 'Справка':
        sg.popup('Данная программа расчитывает принадлежность исследуемого объекта к одному из образов с определенной вероятностью.\n'
                 'Метод расчета был позаимствован из книги "Диагностика кризисного состояния предприятия" автора д.т.н., профессора Я.А.Фомина \n'
                 'Издательство Юнити, Москва 2003, стр. 122-131.\n'
                 '\n'
                 'dndia v.1.0')