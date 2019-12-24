import math
from functools import partial

# сложение векторов
def vector_add(v, w):
		return [v_i + w_i
					 for v_i, w_i in zip(v,w)]

# вычитание векторов
def vector_subtract(v, w):
		return [v_i - w_i
					 for v_i, w_i in zip(v,w)]

# покомпонентная сума списка векторов
def vector_sum(vectors):	# начать с первого вектора
		result = vectors[0]		# пройти в цыкле по остальным векторам
		for vector in vectors[1:]: # и сложить их с результатом
				result = vector_add(result, vector)
		return result

# def vector_sum(vectors):
# 		return reduce(vector_add, vectors)
# vector_add = partial(reduce, vector_add)

# умножение вектора на скаляр
def scalar_multiply(c, v):
		return [c * v_i for v_i in v]

# покомпонентное среднее значение списка векторов
def vector_mean(vectors):
		n = len(vectors)	
		return scalar_multiply(1/n, vector_sum(vectors))	

# скалярно произведение-
# определяет величину на которую вектор v простираеться в направлении вектора w 
def dot (v, w):
		"""v_1*w_1+...+v_n*W_n"""
		return sum(v_i*w_i
							for v_i, w_i in zip(v,w))

# сумма квадратов вектора
# это длина вектора если спроецировать вектор v на вектор w
def sum_of_squares(v):
		""" v_1*v_1+...+v_n*v_n """
		return dot(v, v)

# длина вектора
def magnitude(v): 
		return math.sqrt(sum_of_squares(v))

# евклидово рфсстояние
# """ корень (v_1-w_1)**2+...+(v_n-w_n)**2 """

# квадрат растояния между двумя векторами
def squared_distance(v, w):
		""" (v_1-w_1)**2+...+(v_n-w_n)**2 """
		return sum_of_squares(vector_subtract(v, w))

# растояние между двумя векторами
def distance(v, w):
		""" корень """
		return math.sqrt(squared_distance(v, w))

