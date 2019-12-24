from collections import Counter
from matplotlib import pyplot as plt 
import random
import Probability_theory as pr_ther
import statistics as ind
import matrix as mat
import math


#///////////////////////////////////////////////////////////////////
# одномерные данные
# привести точку данных к номеру интервала
def bucketize(point, bucket_size):
		# округлять точку до следующего наименьшего кратного
		# размера интервала bucket_size
		return bucket_size * math.floor(point / bucket_size)


# подготовить гистограму
def make_histogram(points, bucket_size):
		# сгрупировать точки и подсчитать колитчество в интервале 
		return Counter(bucketize(point, bucket_size) for point in points)

# изобразить гистограму
def plot_histogram(points, bucket_size, title=""):
		histogram = make_histogram(points, bucket_size)
		plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
		plt.title(title)
		plt.show()

# random.seed(0)

# # равномерно распределенные между -100 и 100
# uniform = [200 * random.random() - 100 for _ in range(10000)]

# # нормально распределенные с нулевым средним стандартным отклонением 57
# normal = [57 * pr_ther.inverse_normal_cdf(random.random())
# 				 for _ in range(10000)]

# plot_histogram(uniform, 10, "Гистограма равномерных величин")

# plot_histogram(normal, 10, "Гистограма нормальных величин")


#///////////////////////////////////////////////////////////////////
# двумерные данные

# случайная выборка из нормального распределения
def random_normal():
		return pr_ther.inverse_normal_cdf(random.random())

# xs = [random_normal() for _ in range(1000)]
# ye1 = [x + random_normal() / 2 for x in xs]		
# ye2 = [-x + random_normal() / 2 for x in xs]		

# plt.scatter(xs, ye1, marker='.', color='black', lable='ys1')
# plt.scatter(xs, ye2, marker='.', color='gray', lable='ys2')
# plt.xlabel('xs')
# plt.ylabel('ys')
# plt.legend(loc=9)
# plt.title("очень разное совмесное распределение")
# plt.show()

# print(ind.correlation(xs, ye1)) # 0.9
# print(ind.correlation(xs, ye2)) # -0.9



#///////////////////////////////////////////////////////////////////
# многомерные данные

# корреляцеоная матрица
def correlation_matrix(data):
		# возвращает матрицу num_colums * num_colums где запись
		# в ячейке (i , j ) - это корреляция между столбцами i  и j данных
		_, num_colums = mat.shape(data)
		# pfgbcm d vfnhbwt
		def matrix_entry(i, j):
				return ind.correlation(mat.get_collumn(data, i), mat.get_collumn(data, j))
		return mat.make_matrix(num_colums, num_colums, matrix_entry)


# _, num_colums = mat.shape(data)

# fig, ax = plt.subplot(num_colums, num_colums)

# for i in range(num_colums):
# 		for j in range(num_colums):
# 				# разбросать столбец j по оси x напротив столбца i на оси Y
# 				if i != j: ax[i][j].scatter(mat.get_collumn(data, j), mat.get_collumn(data, i))
# 				# если не i == j показать имя серии 
# 				else: ax[i][j].annotade("серии "+ str(i), (0.5, 0.5),
# 																xycoords='axes fraction',
# 																ha="center", va="center")
# 				# затем спрятать осевые метки за исключением левой нижний диаграмм
# 				if i < num_colums - 1: ax[i][j].xaxis.set_visible(False)
# 				if j > 0: ax[i][j].yaxis.set_visible(False)
# # настроить правую нижнюю и левую верхнюю осевые метки, 
# # которые некоректны потому что на их диаграмы выводяться только текст
# ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
# ax[0][0].set_ylim(ax[0][1].get_ylim())

# plt.show()

# ///////////////////////////////////////////////////////////////////////////
# очистка и формотирование

# разобрать строки табличных данных при помощи анализатора parser(value)
# def parse_row(input_row, parses):
# 		# проиминить анализатор из заданого списка
# 		# к каждому элементу input_row
# 		return [parser(value) if parser is not None else value
# 					 for vlue, parser in zip(input_row, parses)]
									
# разобрать строки табличных данных
def parse_rows_with(reader, parses):
		# обертивает обект reader применяя анализаторы к каждой строке
		for row in reader:
				yield parse_row(row, parses)						

# попытаться разобраться или вернуть none
def try_or_none(f):
		# обертивает функцию f возврвщая none если f вызывает исключение
		# подрозумеваеться что f - функция одного входящего аргумента
		def f_or_none(x):
				try: return f(x)
				except:	return None
		return f_or_none		

# разобрать строки табличных данных при помощи анализатора 
def parse_row(input_row, parses):	
		return [try_or_none(parser)(value) if parser is not None else value
					 for vlue, parser in zip(input_row, parses)]							

# попытаться переобразовать поле в число
def try_parse_field(field_name, value, parser_dict):
		# попытаться пекреобразовать значение при помощи соответствующей
		# функции из словаря parser_dict с анализаторами
		parser = parser_dict.get(field_name) # None если записи нет 
		if parser is not None:
				return try_or_none(parser)(value) 
		else:
				return value

# проанализировать словарь с данными
def parser_dict(input_dict, parser_dict):
		return {field_name: try_parse_field(field_name, value, parser_dict)
					 for field_name, value in input_dict.items()}

#/////////////////////////////////////////////////////////////////
# шкалирование

# стандатизировать данные
def scale(data_matrix):
		# вернуть среднии и стандартные отклонения для каждого столпца
		num_rows, num_cols = mat.shape(data_matrix)			
		mean = [mat.mean(get_column(data_matrix, j))
					 for j in range(num_rows)]		
		stdevs = [standart_deviation(get_column(data_matrix, j))
						 for j in range(num_cols)]		
		return means, stdevs				 				 	  

# создаем новую матрицу
def rescale(data_matrix):
		# прошкалировать входяшие данные так что бы каждый столбец
		# имел среднее значение и стандартное отклонение равное 1
		# пропускает столбци без отклонения
		mean, stdevs = scale(data_matrix)
		# перешкалировать по условию
		def rescaled(i, j):
				if stdevs[j] > 0:
						return (data_matrix[i][j] - means[j] / stdevs[j])
				else:
						return data_matrix[i][j]		

#///////////////////////////////////////////////////////////////////
# снижение размерности

# централизировать матрицу т е вычесть среднее значение
def de_mean_matrix(A):
		# вернуть результат вычесления из каждого значения
		# в А среднього значения столбца
		# Результирующия матрица имеет нулевое среднее в кождом столбце
		nr, nc = mat.shape(A)
		colomn_means, _ = scale(A)			
		return mat.make_matrix(nr, nc, lambda i, j:A[i][j] - colomn_means[j])			

# направление
def direction(w):
		mag = mat.magnitude(w)					# длина вектора
		return [w_i / mag for w_i in w]	#	нормалирование вектора

# направленная дисперсия строки i
def directional_variance_i(x_i, w):
		# дисперсия строки x_i  в направлении определяемом w
		return dot(x_i, direction(w)) ** 2

# направляемая дисперсия данных
def directional_variance(X, w):
		# направляемая дисперсия данных в направлении определяемом w
		return sum(directional_variance_i(x_i, w)
							for x_i in X)	

# градиент направеленой дисперсии строки
def directional_variance_gradient_i(x_i, w):
		# вклад строки x_i в градиент w- направленой дисперсии
		protection_lenght = mat.dot(x_i, direction(w))
		return [2 * protection_lenght * x_ij for x_ij in x_i]

# градиент направеленой дисперсии данных
def directional_variance_gradient(X, w):
		return vec.vector_sum(directional_variance_gradient_i(x_i, w)
												 for x_i in X)

# первая главная компонента
def first_principal_component(X):
		guess = [1 for _ in X[0]]												# предложение
		unscaled_maximizer = maximize_batch(						# нешкалированый масимилизатор
				partical(directional_variance, X),					# теперь это функция w
				partical(directional_variance_gradient, X),	# теперь это функция w
				guess)
		return direction(unscaled_maximizer)		

# здесь нет оси Y поэтому передам вектор состоящий из None
# и функцией которые игнорят данный аргумент
def first_principal_componet(X):
		guess = [1 for _ in X[0]]												# предложение
		unscaled_maximizer = maximize_stochastic(						# нешкалированый масимилизатор
				lambda x, _, w: directional_variance(x,w),
				lambda x, _, w: directional_variance_gradient_i(x,w),
				X,
				[None for _ in X], # фиктивная y
				guess)
		return direction(unscaled_maximizer)	

# спроецировать v на w
def project(v, w):
		# вернуть проецию v на направление w
		projection_lenght = dot(v, w)
		return scalar_multiply(projection_lenght, w)

# удалить проекцию из вектора
def remuve_project_from_vector(c, w):
		# проецырует v на w и вычетает результат из v
		return vector_cubtract(v, project(v, w))

# удалить проекцию из данных
def remuve_projection(X, w):
		# для каждой строки X
		# проецирует строку в w и вычетает результат из строки
		return [remuve_project_from_vector(x_i, w) for x_i in X]	
		
# анализ главных компонет
def principal_component_analysis(X, num_components):
		components = []
		for _ in range(num_components):
				component = first_principal_component(X)
				components.append(component)
				X =remuve_projection(X, component)
		return components			

# трансформировать вектор
def transform_vector(v, components):
		return [dot(v, w) for w in components]

# трансформировать табличные данные
def transform(X, components):
		return [transform_vector(x_i, components) for x_i in X] 					