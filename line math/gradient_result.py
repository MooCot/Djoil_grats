import gradient as gra
import random
from functools import partial
import vector as vec

vector = [13,14,15,16,17,18,19,22,21]


# пример целевой функции: сумма квадратов
# sum_of_squares_result =  gra.sum_of_squares(vector)
# print(sum_of_squares_result)

# отношение приращений

def square(x):
		return x*x

# отношение приращений
# difference_quotient_result =  gra.difference_quotient(square, 2, 2)
# print(difference_quotient_result)

# частичнное отношение приращений
# estimate_gradient_result =  gra.estimate_gradient(square, vector)
# print(estimate_gradient_result)

# derivante_estimate = partial(gra.difference_quotient, square, h=0.00001)
# print(derivante_estimate)

# выбрать произвольную отправную точку
# v = [random.randint(-10, 10) for i in range(3)]


# tolerance = 0.0000001 # константа точности расчета

# while True:
# 		gradient = gra.sum_of_squares_gradient(v) # ВЫЧИСЛИТЬ ГРАДИЕНТ В v
# 		next_v = gra.step(v, gradient, -0.01)   	# сделать отрецательный шаг градиента
# 		if vec.distance(next_v, v) < tolerance: 	# остановиться при достижении
# 				break														# приемлемого уровня (т. е. схождения)
# 		v = next_v

# print(v)

