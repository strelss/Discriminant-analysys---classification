import numpy as np


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

        self.m22_s1 = round(
            (1 / int(self.objs_num_s1)) * (((float(self.evid_s1[3]) - float(self.x_2_s1)) ** 2) + (
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

        self.M1 = np.array([[self.m11_s1, self.m12_s1, self.m13_s1],  # Построение самой ковариационной матрицы
                            [self.m21_s1, self.m22_s1, self.m23_s1],
                            [self.m31_s1, self.m32_s1, self.m33_s1]])
        return self.M1

    def matrix_2(self):
        '''
        Расчет ковариационной матрицы для второго образа (объекта)
        '''
        self.m11_s2 = round((1 / int(self.objs_num_s2)) * (  # TODO: Сделать принцип 0-1-много
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
                    self.x_3_s2))), 2)
        self.m22_s2 = round(
            (1 / int(self.objs_num_s2)) * (((float(self.evid_s2[3]) - float(self.x_2_s2)) ** 2) + (
                    (float(self.evid_s2[4]) - float(self.x_2_s2)) ** 2) +
                                           ((float(self.evid_s2[5]) - float(self.x_2_s2)) ** 2)), 2)
        self.m23_s2 = self.m32_s2 = round((1 / int(self.objs_num_s2)) *
                                          ((float(self.evid_s2[3]) - float(self.x_2_s2)) * (
                                                  float(self.evid_s2[6]) - float(self.x_3_s2)) +
                                           (float(self.evid_s2[4]) - float(self.x_2_s2)) * (
                                                   float(self.evid_s2[7]) - float(self.x_3_s2)) + (
                                                   float(self.evid_s2[5]) - float(
                                               self.x_2_s2)) * (
                                                   float(self.evid_s2[8]) - float(
                                               self.x_3_s2))), 2)
        self.m33_s2 = round(
            (1 / int(self.objs_num_s2)) * (((float(self.evid_s2[6]) - float(self.x_3_s2)) ** 2) + (
                    (float(self.evid_s2[7]) - float(self.x_3_s2)) ** 2) + (
                                                   (float(self.evid_s2[8]) - float(self.x_3_s2)) ** 2)), 2)

        self.M2 = np.array([[self.m11_s2, self.m12_s2, self.m13_s2],  # Построение самой ковариационной матрицы
                            [self.m21_s2, self.m22_s2, self.m23_s2],
                            [self.m31_s2, self.m32_s2, self.m33_s2]])
        return self.M2

    def common_matrix(self):
        '''
        Вычисление общей ковариационной матрицы на основе вычисления предыдущих двух методов
        '''
        self.M1 = self.matrix_1()
        self.M2 = self.matrix_2()

        M = (1 / (self.objs_num_s1 + self.objs_num_s2 - 2)) * (self.objs_num_s1 * self.M1 + self.objs_num_s2 * self.M2)
        return M

    def inverse_covariance_matrix(self):
        '''
        Вычисление обратной ковариационной матрицы
        '''
        self.a = self.common_matrix()
        self.inv_M = np.linalg.inv(self.a)
        print(self.inv_M)
        return self.inv_M