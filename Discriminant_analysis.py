import PySimpleGUI as sg
import numpy as np
from discrim_module import average_vectors as vec
from discrim_module import covar_matrix as cov_mat

col_obj1 = [
    [sg.Text('', size=(23, 1)), sg.Text('Образ S\u00b9', size=(10, 1))],
    [sg.Text('', size=(8, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)),
     sg.Text('Объект obj\u2081', size=(10, 1)), ],
    [sg.Text('Признак x\u2081'), sg.Input('31.33', size=(11, 1), key='s1X1x1'),
     sg.Input('32.78', size=(11, 1), key='s1X2x1'), sg.Input('35.61', size=(11, 1), key='s1X3x1'), ],
    [sg.Text('Признак x\u2082'), sg.Input('4.15', size=(11, 1), key='s1X1x2'),
     sg.Input('3.34', size=(11, 1), key='s1X2x2'), sg.Input('5.56', size=(11, 1), key='s1X3x2'), ],
    [sg.Text('Признак x\u2083'), sg.Input('79', size=(11, 1), key='s1X1x3'), sg.Input('81', size=(11, 1), key='s1X2x3'),
     sg.Input('82', size=(11, 1), key='s1X3x3'), ],
]

col_obj2 = [
    [sg.Text('', size=(23, 1)), sg.Text('Образ S\u00b2', size=(10, 1))],
    [sg.Text('', size=(8, 1)), sg.Text('Объект obj\u2081', size=(10, 1)), sg.Text('Объект obj\u2081', size=(10, 1)),
     sg.Text('Объект obj\u2081', size=(10, 1)), ],
    [sg.Text('Признак x\u2081'), sg.Input('12.25', size=(11, 1), key='s2X1x1'),
     sg.Input('13.09', size=(11, 1), key='s2X2x1'), sg.Input('7.65', size=(11, 1), key='s2X3x1'), ],
    [sg.Text('Признак x\u2082'), sg.Input('2.98', size=(11, 1), key='s2X1x2'),
     sg.Input('3.01', size=(11, 1), key='s2X2x2'), sg.Input('2.38', size=(11, 1), key='s2X3x2'), ],
    [sg.Text('Признак x\u2083'), sg.Input('66', size=(11, 1), key='s2X1x3'), sg.Input('69', size=(11, 1), key='s2X2x3'),
     sg.Input('58', size=(11, 1), key='s2X3x3'), ],
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
    [sg.Output(size=(88, 20))],
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
        evid_s1 = (values['s1X1x1'], values['s1X2x1'], values['s1X3x1'],
                   values['s1X1x2'], values['s1X2x2'], values['s1X3x2'],
                   values['s1X1x3'], values['s1X2x3'], values['s1X3x3'])

        evid_s2 = (values['s2X1x1'], values['s2X2x1'], values['s2X3x1'],
                   values['s2X1x2'], values['s2X2x2'], values['s2X3x2'],
                   values['s2X1x3'], values['s2X2x3'], values['s2X3x3'])


        def main():
            a = vec.Middle_Vektor(3, 3, 3, 3, evid_s1, evid_s2)
            a = a.give()
            print(a)
            print('-------')
            b = cov_mat.Kovar_Matrix(a[2], a[3], a[4], a[5], a[6], a[7], evid_s1, evid_s2, 3, 3, 3, 3)
            b.inverse_covariance_matrix()



        main()
        # sg.popup('Testing complete')
