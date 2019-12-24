

# функция прогнозирования
def predict(alpha, beta, x_i):
		return beta * x_i + alpha

# вернуть ошибку т е отклонение наблюдаемого значения
# зависимой переменной y_i от модельных значений predict
def error(alpha, beta, x_i, y_i):
		# ошбка в результате прогнозирования beta * x_i + alpha
		# принаблюдаемом значении y_i
		return y_i - predict(alpha, beta, x_i) 

# сумма квадратичных ошибок
def sum_of_squared_errors(alpha, beta, x, y):
		return sum(error(alpha, beta, x_i, y_i) ** 2
							for x_i, y_i in zip(x, y))

# подгонка методом найменьших квадратов
def least_squares_fit(x, y):
		# при заданых обучающих значениях x и y
		# найти значения alpha и beta на основе МНК
		beta =correlation(x * y) * standart_deviation(y) / standart_deviation(x)
		alpha = mean(y) - beta * mean(x)
		return alpha, beta

# полная сума квадратов
def total_sum_of_squares(y):
		# полная сума квадратов отклонений y_i от их среднего
		return sum(v ** 2 for v in de_mean(y))

# р-квадрат - это доля вариации зависимой переменной обясняемая моделью
def r_squared(alpha, beta, x, y):		
		# доля вариации в y обясняемая моделью равна 
		# 1-доля вариации в y не обясняемая моделью
		return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / 
								 total_sum_of_squares(y))

# квадратическая ошибка
def squared_error(x_i, y_i, theta):
		alpha, beta = theta
		return error(alpha, beta, x_i, y_i) ** 2								 

# градиент квадратичной ошибки
def squared_error_gradient(x_i, y_i, theta):		
		alpha, beta = theta
		# частичные производные alpha, и beta
		return [-2 * error(alpha, beta, x_i, y_i),
						-2 * error(alpha, beta, x_i, y_i) * x_i]