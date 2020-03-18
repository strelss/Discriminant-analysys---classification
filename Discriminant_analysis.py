import PySimpleGUI as sg
import numpy as np

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

        class Middle_Vektor:
            '''
            Этот класс вычисляет оценки векторов средних а1 и а2 в виде матриц,
            состоящих из одного столбца и трех строк (ну или элементов, до задницы кароч)
            '''
            def __init__(self, objs_num_s1, evs_num_s1, objs_num_s2, evs_num_s2, evid1, evid2):
                self.objs_num_s1 = objs_num_s1
                self.evs_num_s1 = evs_num_s1
                self.objs_num_s2 = objs_num_s2
                self.evs_num_s2 = evs_num_s2
                self.evid_s1 = evid1
                self.evid_s2 = evid2

            def give(self):
                '''
                Метод отдает оценки векторов средних в виде матриц
                :return:
                '''
                self.x_1_s1_sum = 0  # TODO: сделать в будущем самоопределение по количеству признаков
                self.x_2_s1_sum = 0
                self.x_3_s1_sum = 0
                self.i = 0
                while self.i < self.objs_num_s1:
                    self.x_1_s1_sum += float(self.evid_s1[self.i])  # Усредненный показателя х_1_s1_sum
                    self.x_2_s1_sum += float(
                        self.evid_s1[self.i + self.objs_num_s1])  # Усредненный показателя х_2_s1_sum
                    self.x_3_s1_sum += float(
                        self.evid_s1[self.i + self.objs_num_s1 * 2])  # Усредненный показателя х_3_s1_sum
                    self.i += 1

                self.x_1_s2_sum = 0
                self.x_2_s2_sum = 0
                self.x_3_s2_sum = 0
                self.i = 0
                while self.i < self.objs_num_s2:
                    self.x_1_s2_sum += float(self.evid_s2[self.i])  # Усредненный показателя х_1_s2_sum
                    self.x_2_s2_sum += float(
                        self.evid_s2[self.i + self.objs_num_s2])  # Усредненный показателя х_2_s2_sum
                    self.x_3_s2_sum += float(
                        self.evid_s2[self.i + self.objs_num_s2 * 2])  # Усредненный показателя х_3_s2_sum
                    self.i += 1


                self.x_1_s1 = round((1 / self.objs_num_s1) * self.x_1_s1_sum, 3)  # элементы матницы а1
                self.x_2_s1 = round((1 / self.objs_num_s1) * self.x_2_s1_sum, 3)
                self.x_3_s1 = round((1 / self.objs_num_s1) * self.x_3_s1_sum, 3)  # TODO: сделать в будущем самоопределение по количеству признаков, как и вверху

                self.x_1_s2 = round((1 / self.objs_num_s1) * self.x_1_s2_sum, 3)  # элементы матницы а2
                self.x_2_s2 = round((1 / self.objs_num_s1) * self.x_2_s2_sum, 3)
                self.x_3_s2 = round((1 / self.objs_num_s1) * self.x_3_s2_sum, 3)

                self.a1 = np.array([[self.x_1_s1], [self.x_2_s1], [self.x_3_s1]])
                self.a2 = np.array([[self.x_1_s2], [self.x_2_s2], [self.x_3_s2]])

                return self.a1, self.a2, self.x_1_s1, self.x_2_s1, self.x_3_s1, self.x_1_s2, self.x_1_s2, self.x_1_s2,


        class Kovar_Matrix:
            def __init__(self):
                pass


        def main():
            a = Middle_Vektor(3, 3, 3, 3, evid_s1, evid_s2)
            b = a.give()

        main()
        # sg.popup('Testing complete')
