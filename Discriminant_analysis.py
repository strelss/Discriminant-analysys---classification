import PySimpleGUI as sg
import numpy as np
from discrim_module import average_vectors as vec

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


        class Kovar_Matrix:
            '''
            Расчет ковариационных матиц для первого и второго образа (объекта),
            а потом и оценка общей ковариационной матрицы
            '''

            def __init__(self, x_1_s1, x_2_s1, x_3_s1, x_1_s2, x_2_s2, x_3_s2, evid_s1, evid_s2, objs_num_s1,
                         evs_num_s1, objs_num_s2, evs_num_s2):
                self.x_2_s1 = x_2_s1
                self.x_3_s1 = x_3_s1
                self.x_1_s1 = x_1_s1
                self.x_2_s2 = x_2_s2
                self.x_3_s2 = x_3_s2
                self.x_1_s2 = x_1_s2
                self.evid_s1 = evid_s1
                self.evid_s2 = evid_s2
                self.objs_num_s1 = objs_num_s1
                self.evs_num_s1 = evs_num_s1
                self.objs_num_s2 = objs_num_s2
                self.evs_num_s2 = evs_num_s2

            def matrix_1(self):
                '''
                Расчет ковариационной матрицы для первого образа (объекта)
                '''
                self.m11_s1 = round((1 / int(self.objs_num_s1)) * (  # TODO: Сделать принцип 0-1-много
                        ((float(self.evid_s1[0]) - float(self.x_1_s1)) ** 2) + (
                    # Вычисление коефициентов матрицы первого образа
                        (float(self.evid_s1[1]) - float(self.x_1_s1)) ** 2) + (
                                (float(self.evid_s1[2]) - float(self.x_1_s1)) ** 2)), 2)

                self.m12_s1 = self.m21_s1 = round(
                    (1 / int(self.objs_num_s1)) * ((float(self.evid_s1[0]) - float(self.x_1_s1)) * (
                            float(self.evid_s1[3]) - float(self.x_2_s1)) + (
                                                               float(self.evid_s1[1]) - float(self.x_1_s1)) * (
                                                           float(self.evid_s1[4]) - float(
                                                       self.x_2_s1)) + (
                                                           float(self.evid_s1[2]) - float(
                                                       self.x_1_s1)) * (
                                                           float(self.evid_s1[5]) - float(
                                                       self.x_2_s1))), 2)

                self.m13_s1 = self.m31_s1 = round((1 / int(self.objs_num_s1)) * (
                            (float(self.evid_s1[0]) - float(self.x_1_s1)) * (
                            float(self.evid_s1[6]) - float(self.x_3_s1)) + (
                                        float(self.evid_s1[1]) - float(self.x_1_s1)) * (
                                    float(self.evid_s1[7]) - float(
                                self.x_3_s1)) + (
                                    float(self.evid_s1[2]) - float(
                                self.x_1_s1)) * (
                                    float(self.evid_s1[8]) - float(
                                self.x_3_s1))), 2)

                self.m22_s1 = round((1 / int(self.objs_num_s1)) * (((float(self.evid_s1[3]) - float(self.x_2_s1)) ** 2) + (
                        (float(self.evid_s1[4]) - float(self.x_2_s1)) ** 2) +
                                                             ((float(self.evid_s1[5]) - float(self.x_2_s1)) ** 2)), 2)

                self.m23_s1 = self.m32_s1 = round((1 / int(self.objs_num_s1)) * (
                            (float(self.evid_s1[3]) - float(self.x_2_s1)) * (
                            float(self.evid_s1[6]) - float(self.x_3_s1)) + (
                                        float(self.evid_s1[4]) - float(self.x_2_s1)) * (
                                    float(self.evid_s1[7]) - float(
                                self.x_3_s1)) + (
                                    float(self.evid_s1[5]) - float(
                                self.x_2_s1)) * (
                                    float(self.evid_s1[8]) - float(
                                self.x_3_s1))), 2)

                self.m33_s1 = round((1 / int(self.objs_num_s1)) * (
                        ((float(self.evid_s1[6]) - float(self.x_3_s1)) ** 2) + (
                        (float(self.evid_s1[7]) - float(self.x_3_s1)) ** 2) + (
                                (float(self.evid_s1[8]) - float(self.x_3_s1)) ** 2)), 2)


                M1 = np.array([[self.m11_s1, self.m12_s1, self.m13_s1],  # Построение самой ковариационной матрицы
                               [self.m21_s1, self.m22_s1, self.m23_s1],
                               [self.m31_s1, self.m32_s1, self.m33_s1]])
                print(M1)

            def matrix_2(self):
                '''
                Расчет ковариационной матрицы для второго образа (объекта)
                '''
                self.m11_s2 = round((1 / int(self.objs_num_s2)) * (                 # TODO: Сделать принцип 0-1-много
                        ((float(self.evid_s2[0]) - float(self.x_1_s2)) ** 2) + (
                                                                                    # Вычисление коефициентов матрицы второго образа
                        (float(self.evid_s2[1]) - float(self.x_1_s2)) ** 2) + (
                                (float(self.evid_s2[2]) - float(self.x_1_s2)) ** 2)), 2)
                self.m12_s2 = self.m21_s2 = round((1 / int(self.objs_num_s2)) * (
                            (float(self.evid_s2[0]) - float(self.x_1_s2)) * (
                            float(self.evid_s2[3]) - float(self.x_2_s2)) + (
                                        float(self.evid_s2[1]) - float(self.x_1_s2)) * (
                                    float(self.evid_s2[4]) - float(
                                self.x_2_s2)) + (
                                    float(self.evid_s2[2]) - float(
                                self.x_1_s2)) * (
                                    float(self.evid_s2[5]) - float(
                                self.x_2_s2))), 2)
                self.m13_s2 = self.m31_s2 = round((1 / int(self.objs_num_s2)) * (
                            (float(self.evid_s2[0]) - float(self.x_1_s2)) * (
                            float(self.evid_s2[6]) - float(self.x_3_s2)) + (
                                        float(self.evid_s2[1]) - float(self.x_1_s2)) * (
                                    float(self.evid_s2[7]) - float(
                                self.x_3_s2)) + (
                                    float(self.evid_s2[2]) - float(
                                self.x_1_s2)) * (
                                    float(self.evid_s2[8]) - float(
                                self.x_3_s2))),2)
                self.m22_s2 = round((1 / int(self.objs_num_s2)) * (((float(self.evid_s2[3]) - float(self.x_2_s2)) ** 2) + (
                        (float(self.evid_s2[4]) - float(self.x_2_s2)) ** 2) +
                                                             ((float(self.evid_s2[5]) - float(self.x_2_s2)) ** 2)), 2)
                self.m23_s2 = self.m32_s2 = round((1 / int(self.objs_num_s2)) *
                                            ((float(self.evid_s2[3]) - float(self.x_2_s2)) * (float(self.evid_s2[6]) - float(self.x_3_s2)) +
                                                        (float(self.evid_s2[4]) - float(self.x_2_s2)) * (
                                    float(self.evid_s2[7]) - float(self.x_3_s2)) + (
                                    float(self.evid_s2[5]) - float(
                                self.x_2_s2)) * (
                                    float(self.evid_s2[8]) - float(
                                self.x_3_s2))), 2)
                print(self.m23_s2, self.m32_s2)
                self.m33_s2 = round((1 / int(self.objs_num_s2)) * (((float(self.evid_s2[6]) - float(self.x_3_s2)) ** 2) + (
                        (float(self.evid_s2[7]) - float(self.x_3_s2)) ** 2) + (
                                (float(self.evid_s2[8]) - float(self.x_3_s2)) ** 2)), 2)

                M2 = np.array([[self.m11_s2, self.m12_s2, self.m13_s2],  # Построение самой ковариационной матрицы
                               [self.m21_s2, self.m22_s2, self.m23_s2],
                               [self.m31_s2, self.m32_s2, self.m33_s2]])
                print(M2)
                # TODO: Написать код, который вычисляет общую ковариационную матрицу


        def main():
            a = vec.Middle_Vektor(3, 3, 3, 3, evid_s1, evid_s2)
            a = a.give()
            print(a)
            print('-------')
            b = Kovar_Matrix(a[2], a[3], a[4], a[5], a[6], a[7], evid_s1, evid_s2, 3, 3, 3, 3)
            b.matrix_1()
            b.matrix_2()


        main()
        # sg.popup('Testing complete')
