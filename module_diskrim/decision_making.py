import numpy as np


class Decision_making:
    '''
    Этап принятия решения. Вычисления оценки логарифма отношения правдоподобия
    и подставление найденного значения в решающее правило
    '''

    def __init__(self, a1, a2, M, n, X):
        self.a1 = a1
        self.a2 = a2
        self.M = M
        self.n = n
        self.X = X

        print()
        print('Инициализация модуля второго этапа.')
        print()
        print('Второй этап: принятие решения.')
        print('Вычисление:')
        print('     оценки логарифма отношения правдоподобия lnL\u0302;')
        print('     подстановка найденного значения в решающее правило lnC = 0;')
        print('     составление вывода.')
        print()

    def first_multipler(self):
        '''
        Вычисление первого сомножителя. Разность векторов средних и их транспонирование,
        умножение на обратную ковариационную матрицу
        '''
        self.dif_a = self.a1 - self.a2
        self.tr_dif_a = np.transpose(self.dif_a)
        self.fir_mul = np.dot(self.tr_dif_a, self.M)
        return self.fir_mul

    def second_multipler(self):
        self.X_vec = np.transpose(np.array([self.X]))
        self.X_vec = np.dot(self.X_vec, 2)
        self.sum_a = self.a1 + self.a2
        self.sec_mul = self.X_vec - self.sum_a
        return self.sec_mul

    def decision(self):
        self.a_t = np.transpose(self.first_multipler())
        self.b_t = self.second_multipler()
        self.dec = self.a_t * self.b_t
        self.dec = (self.dec[0 ] +self.dec[1 ] +self.dec[2] ) /2
        self.obj = 0
        if self.dec > 0:
            print('lnL\u0302 = ' + str(self.dec) + ' > 0')
            print()
            print('Результаты вычислений свидетельствуют о том, что исследуемый объект \u1E8C принадлежит образу S\u00b9.')
            print()
            self.obj = 1
        elif self.dec < 0:
            print('lnL\u0302 = ' + str(self.dec) + ' < 0')
            print()
            print('Результаты вычислений свидетельствуют о том, что исследуемый объект \u1E8C принадлежит образу S\u00b2.')
            print()
            self.obj = 2
        print('Второй модуль вычислений завершен.')
        print('______________________________________________________________________________________________')
        print()
        return self.dec, self.obj