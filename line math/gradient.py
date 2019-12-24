import random

# градиент


# пример целевой функции: сумма квадратов
def sum_of_squares(v):
		# вычисляет сумму квадратов элемента вектора v
		return sum(v_i ** 2 for v_i in v)

# отношение приращений
def difference_quotient(f, x, h):
		return (f(x + h) - f(x)) / h

# частичнное отношение приращений
def partial_difference_quotient(f, v, i, h):
		#	вычислить i-ое частичное отношение приращений функции f в векторе v
		w = [v_j + (h if j == i else 0) # прибавить h только к i-му элементу v
				for j, v_j in enumerate(v)]
		return (f(w) - f(v)) / h		

# оценить градиент
def estimate_gradient(f, v, h=0.00001):
		return [partial_difference_quotient(f, v, i,h)
					 for i, _ in enumerate(v)]		

# сделать шаг градиента
def step(v, direction, step_size):
		#	двигаться с шагом размером step_size в направлении от v
		return [v_i + step_size * direction_i
					 for v_i, direction_i in zip(v, direction)]				

# градиент суммы квадратов
def sum_of_squares_gradient(v):
		return [2 * v_i for v_i in v]

# выбрать произвольную отправную точку
# v = [random.randint(-10, 10) for i in range(3)]

# tolerance = 0.0000001 # константа точности расчета

# while True:
# 		gradient = sum_of_squares_gradient(v) # ВЫЧИСЛИТЬ ГРАДИЕНТ В	v
# 		next_v = step(v, gradient, -0.01)   	# сделатьотрецательный шаг градиента
# 		if distance(next_v, v) < tolerance: 	# остановиться при достижении
# 				break 														# приемлемого уровня (т. е. схождения)
# 		v = next_v														# продолжить если нет

# безопасная версия
def safe(f):
		# вернуть новую функцию одинаковую с f за исключением
		# того что она возвращает бесконечность всякий раз когда она выдает ошибку
		def safe_f(*args, **kwards):
				try:
						return f(*args, **kwards)
				except:
						return float('int') # питон бесконечность
				return safe_f				 

# пакетная минимизация
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.00001):	
		# использует градиентный спуск для нахождения вектора theta . который
		# минимизирует целевую функцию target_fn			
		step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
		theta = theta_0 						# установить тэта в начальное значение
		target_fn = safe(target_fn) # безопасная версия
																# целевой функции target_fn
		value = target_fn(theta) 		# минимизируемое значение

		while True:
					gradient = gradient_fn(theta)
					next_thetas = [step(theta, gradient, -step_size)
												for step_size in step_sizes]
					# выбрать то котороя минимизирует функцию ошибок
					next_theta = min(next_thetas, key = target_fn)
					next_value = target_fn(next_theta)

					# остановиться если функция сходиться 
					if abs(value - next_value) < tolerance: # меньше константы точности?
							return theta
					else: 
							theta, value = next_theta, next_value								

# отрицание результата на выходе
def negate(f):
		# вернуть функцию которая для любого входящего х возврощает -f(x)
		return lambda *args, **kwards: -f(*args, **kwards)							

# отрицание списка результатов на выходе
def negate_all(f):
		# то же. когда f возвращает список чисел		
		return lambda *args, **kwards: [-y for y in f(*args, **kwards)]

# пакетная максимизация путем минимизациии отрицания
def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.00001):
		return minimize_batch(negate(target_fn),
													negate_all(gradient_fn),
													tolerance)		


#//////////////////////////////////////////////////////////////////////
# стохастический градиентный спуск

# перемешать индекксы
def in_random_order(data):
		# генератор который возвращает элементы в случайном порядке
		indexes=[i for i, _ in enumerate(data)] # создать список индексов
		random.shuffle(indexes)								  # перемешать данные и
		for i in indexes: 											#	вернуть в этом порядке 			
				yield data[i]

# стохастическая минимизация
def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
		data = zip(x, y) 
		theta = theta_0  # первоначальная гипотеза			
		alpha = alpha_0  # первоначальный размер шага
		min_theta, min_value = None, float("inf") # минимум на этот момент
		iterations_with_no_improvement = 0

		# остановиться если достигли 100 итераций без улучшений
		while iterations_whith_no_improvement < 100:
				value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

				if value < min_value:
						# если найден новый минимум. то запомнить его
						# и вернуться к первоначальному размеру шага
						min_theta, min_value = theta, value
						iterations_with_no_improvement = 0
						alpha = alpha_0
				else:
						# в противном случае улучшений нет
						# поэтому пытаемся сжать размер шага
						iterations_with_no_improvement += 1
						alpha *= 0.9

						# и делаем шаг градиента для каждой из точек данныч
						for x_i, y_i in in_random_orther(data):
								gradient_i = gradient_fn(x_i, y_i, theta)
								theta = vector_substract(theta, 
																				scalar_multiply(alpha, gradient_i))
		return min_theta																		 		

# стохастическая максимилизация
def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
		return maximize_stochastic(negate(target_fn),
															negate_all(gradient_fn),
															x, y, theta_0, alpha_0)