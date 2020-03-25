import math
import numpy as np

class Diagnostic_assessment:
    '''
    Расчет оценки достоверности диагностики. Вычисляются оценки первого и второго рода.
    Для этого вычисляются: расстояние Махаланобиса, стандартное отклонение 1, 2 и функции от них, а именно экспонента и интеграл Лапласа
    '''
    def __init__(self, a1, a2, inv_M, m1, m2, n):
        self.a1 = a1
        self.a2 = a2
        self.inv_M = inv_M
        self.m1 = m1
        self.m2 = m2
        self.n = n

    def distance_Mahalanobise(self):  # Раочет расстояния Махаланобиса
        self.dif_a = self.a1 - self.a2
        self.tr_dif_a = np.transpose(self.dif_a)
        self.fir_mul = np.dot(self.tr_dif_a, self.inv_M)
        # print(self.dif_a)
        # print()
        # print(self.fir_mul)
        self.dis_Mahal_quad = self.dif_a[0 ] *self.fir_mul[0][0] + self.dif_a[1 ] *self.fir_mul[0][1] + self.dif_a[2 ] \
                              *self.fir_mul[0][2]
        self.dis_Mahal = round(math.sqrt(self.dis_Mahal_quad), 2)
        # print(self.dis_Mahal_quad)
        return self.dis_Mahal


    def skv(self):  # Расчет стандартного отклонения 1 и 2
        self.sig_1 = round(math.sqrt((1 / self.m1) + (1 / self.m2)), 2)
        self.sig_2 = round(math.sqrt((1 / self.m1) + (1 / self.m2) + (4 / self.n)), 2)
        # print(self.sig_2)
        return self.sig_1, self.sig_2

    def func_Laplase_exp(self):
        '''
        Расчет функции Лапласа и экспонент, так же возвращает возвращает значения расчета функции Махаланаболиза и стандартных отклонений
        '''
        self.d = self.distance_Mahalanobise()
        self.sig = self.skv()
        self.sig_1 = self.sig[0]
        self.sig_2 = self.sig[1]
        self.F1 = math.erf(self.d / self.sig_1)
        self.F2 = 1 - math.erf(self.d / self.sig_1)
        self.F3 = math.erf(self.d / self.sig_2)
        self.F4 = 1 - math.erf(self.d / self.sig_2)
        self.exp_1 = round(math.exp(-((self.d ** 2) / 2 * (self.sig_1 ** 2))), 5)
        self.exp_2 = round(math.exp(-((self.d ** 2) / 2 * (self.sig_2 ** 2))), 5)
        return self.d, self.sig_1, self.sig_2, self.F1, self.F2, self.F3, self.F4, self.exp_1, self.exp_2

    def main(self):
        '''
        Главный метод, запускает предыдущие методы и выдает вероятность достоверности рассчитанных данных
        '''
        self.all_var = self.func_Laplase_exp()
        self.probab_mist = self.all_var[3] * self.all_var[6] + self.all_var[4] * self.all_var[5] + \
                           ((self.all_var[1] * self.all_var[2]) /
                                       (2.5 * self.all_var[0] * (self.all_var[1] ** 2 - self.all_var[2] ** 2))) * \
                           (self.all_var[2] * self.all_var[7] * (self.all_var[5] - self.all_var[6]) - self.all_var[1] *
                            self.all_var[8] * (self.all_var[3] - self.all_var[4]))
        self.veracity = 1 - self.probab_mist
        print(self.veracity)