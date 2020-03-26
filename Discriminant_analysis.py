import PySimpleGUI as sg
import numpy as np
import math
from discrim_module import average_vectors as vec
from discrim_module import covar_matrix as cov_mat
from discrim_module import decision_making as dec_mak
from discrim_module import diagnostic_assessment as  dia_as

col_obj1 = [
    [sg.Text('', size=(23, 1)), sg.Text('Образ S\u00b9', size=(10, 1))],
    [sg.Text('', size=(8, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)),
     sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), ],
    [sg.Text('Признак x\u2081'), sg.Input('31.33', size=(11, 1), key='s1X1x1'),
     sg.Input('32.78', size=(11, 1), key='s1X2x1'), sg.Input('35.61', size=(11, 1), key='s1X3x1'), sg.Input('30.54', size=(11, 1), key='s1X4x1'), ],
    [sg.Text('Признак x\u2082'), sg.Input('4.15', size=(11, 1), key='s1X1x2'),
     sg.Input('3.34', size=(11, 1), key='s1X2x2'), sg.Input('5.56', size=(11, 1), key='s1X3x2'), sg.Input('4.76', size=(11, 1), key='s1X4x2'), ],
    [sg.Text('Признак x\u2083'), sg.Input('79', size=(11, 1), key='s1X1x3'), sg.Input('81', size=(11, 1), key='s1X2x3'),
     sg.Input('82', size=(11, 1), key='s1X3x3'), sg.Input('80', size=(11, 1), key='s1X4x3'), ],
]

col_obj2 = [
    [sg.Text('', size=(23, 1)), sg.Text('Образ S\u00b2', size=(10, 1))],
    [sg.Text('', size=(8, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)),
     sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), ],
    [sg.Text('Признак x\u2081'), sg.Input('12.25', size=(11, 1), key='s2X1x1'),
     sg.Input('13.09', size=(11, 1), key='s2X2x1'), sg.Input('7.65', size=(11, 1), key='s2X3x1'), sg.Input('9.98', size=(11, 1), key='s2X4x1'), sg.Input('8.77', size=(11, 1), key='s2X5x1'), ],
    [sg.Text('Признак x\u2082'), sg.Input('2.98', size=(11, 1), key='s2X1x2'),
     sg.Input('3.01', size=(11, 1), key='s2X2x2'), sg.Input('2.38', size=(11, 1), key='s2X3x2'),  sg.Input('2.73', size=(11, 1), key='s2X4x2'),  sg.Input('2.91', size=(11, 1), key='s2X5x2'), ],
    [sg.Text('Признак x\u2083'), sg.Input('66', size=(11, 1), key='s2X1x3'), sg.Input('69', size=(11, 1), key='s2X2x3'),
     sg.Input('58', size=(11, 1), key='s2X3x3'), sg.Input('71', size=(11, 1), key='s2X4x3'), sg.Input('55', size=(11, 1), key='s2X5x3'), ],
    [sg.Text('', size=(1, 2))]
]

research_obj = [
    [sg.Text('', size=(1, 1))],
    [sg.Text('', size=(1, 1)), sg.Text('Исследуемый объект \u1E8C', size=(20, 1))],
    [sg.Text('Признак x\u2081'), sg.Input('33.21', size=(11, 1), key='s3x1')],
    [sg.Text('Признак x\u2082'), sg.Input('5.58', size=(11, 1), key='s3x2')],
    [sg.Text('Признак x\u2083'), sg.Input('79', size=(11, 1), key='s3x3')],
]

layout = [
    [sg.Column(col_obj1), sg.Column(research_obj)],
    [sg.Column(col_obj2)],
    [sg.Output(size=(95, 20))],
    [sg.Submit('Начать исследование'), sg.Cancel('Выход')]
]
window = sg.Window('Discriminant_classification', layout)
print('Testing')

while True:  # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
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


                    #TODO: доделать интерфейс и справку. Доделать вывод расчетных данных в лог.



        def main():
            a = vec.Middle_Vektor(4, 3, 5, 3, evid_s1, evid_s2)
            a = a.give()

            # print(a)
            # print('-------')

            b = cov_mat.Kovar_Matrix(a[2], a[3], a[4], a[5], a[6], a[7], evid_s1, evid_s2, 4, 3, 5, 3)
            b = b.inverse_covariance_matrix()
            # print(b)
            #
            #
            c = dec_mak.Decision_making(a[0], a[1], b, 1, evid_s3)
            # c1 = c.first_multipler()
            # # print(c1)
            # # print('-------------')
            c2 = c.decision()
            # print()
            # print('_-_-_-_-_-_-_-_-')
            # print()
            # print(c2)
            d = dia_as.Diagnostic_assessment(a[0], a[1], b, 4, 5, 1)
            d = d.main()
            # print(d)
            print()
            print('В результате вычислений сделан такой вывод: ')
            if c2[1] == 1:
                print()
                print('        исследуемый объект \u1E8C принадлежит к образу S\u00b9 с вероятностью ' + str(d))
            elif c2[1] == 2:
                print()
                print('        исследуемый объект \u1E8C принадлежит к образу S\u00b2 с вероятностью ' + str(d))
            print()
            print('Исследование завершено.')
        main()
