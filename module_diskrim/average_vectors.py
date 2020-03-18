import numpy as np


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
        self.x_3_s1 = round((1 / self.objs_num_s1) * self.x_3_s1_sum,
                            3)  # TODO: сделать в будущем самоопределение по количеству признаков, как и вверху

        self.x_1_s2 = round((1 / self.objs_num_s1) * self.x_1_s2_sum, 3)  # элементы матницы а2
        self.x_2_s2 = round((1 / self.objs_num_s1) * self.x_2_s2_sum, 3)
        self.x_3_s2 = round((1 / self.objs_num_s1) * self.x_3_s2_sum, 3)

        self.a1 = np.array([[self.x_1_s1], [self.x_2_s1], [self.x_3_s1]])
        self.a2 = np.array([[self.x_1_s2], [self.x_2_s2], [self.x_3_s2]])

        return self.a1, self.a2, self.x_1_s1, self.x_2_s1, self.x_3_s1, self.x_1_s2, self.x_1_s2, self.x_1_s2,