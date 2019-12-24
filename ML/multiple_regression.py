import random


# множественная регресия

# 
def predict(x_i, beta):
		#передполагаеться что первый элемент каждого x_i = 1
		return dot(x_i, beta)

# функция ошибок
def error(x_i, y_i, beta):
		return y_i - predict(x_i, beta)

# квадратичная ошибка
def squared_error(x_i, y_i, beta):
		return error(x_i, y_i, beta) ** 2

# градиент квадратичной ошибки
def squared_error_gradient(x_i, y_i, beta):
		# градиент относительно beta соотведствующий i - ому квадрату ошибки
		return [-2 * x_ij * error(x_i, y_i, beta)
					 for x_ij in x_i]			

# оценить beta
def estimate_beta(x, y):
		beta_intial = [random.random() for x_i in x[0]]
		return minimize_stochastic(
			squared_error,
			squared_error_gradient,
			x, y,
			beta_intial,
			0.001
		)			

# многофакторный R квадрат
def multiple_r_squared(x, y, beta):
		sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2
															 for x_i, y_i in zip(x, y))
		return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)			

# выбрка на основе бутстрап метода
def bootstrap_sample(data):
		# случайн выбирает len(data) элементов с возвратом
		return [random.choice(data) for _ in data]				

# статистика на основе бутрстап метода
def bootstrap_statistic(data, stats_fn, num_samples):
		# оценивает функцию stats_fn на бутстрап выборках 
		#  из данных в количестве nu_samples
		return [stats_fn(bootstrap_sample(data))
					 for _ in range(num_samples)] 

# оценить beta для выборки
def estimate_sample_beta(sample):
		# выборка представлена списком пар (x_i, y_i)
		x_sample, y_sample = zip(*sample) # трюк с разоединением списка
		return estimate_beta(x_sample, y_sample)

# p-значение
def p_value(beta_hat_j, sigma_hat_j):
		if beta_hat_j > 0:
				# если коэфициент имеет положительное значение
				# нужно дважды вычеслить вероятность 
				# наблюдать еще более крупное значение
				return 2 * (1 - normal_cdf(beta_hat_j / sigma_hat_j))
		else:
				# в противном случае вероятность наблюдать меньшее значение
				return 2 * normal_cdf(beta_hat_j / sigma_hat_j)		

# alpha гипер параметр контролирующий насколько жестким будет штраф(лямбда параметр)
def ridge_penalty(beta, alpha):
		return alpha * dot(beta[1:], beta[1:])

# квадратичная ошибка гребневой регресии
def squared_error_ridge(x_i, y_i, beta, alpha):
		# оценить ошибку + штраф для beta
		return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha) 	

# градиент гребневого штрафа
def ridge_penalty_gradient(beta, alpha):
		return [0] + [2 * alpha * beta_j for beta_j in beta[1:]]

def squared_error_ridge_gradient(x_i, y_i, beta, alpha):
		# градиент соответствующий i -й ошибке
		# включая гребневый штраф
		return vector_add(squared_error_gradient(x_i, y_i, beta),
										 ridge_penalty_gradient(beta, alpha))		

# оценить beta гребневой функции
def estimate_beta_ridge(x, y, alpha):
		# применить градиентный спуск для подгонки гребневой регрессии
		# со штрафом alpha
		beta_intial = [random.random() for x_i in x[0]]
		return minimize_stochastic(partial(squared_error_ridge, alpha=alpha),
															 partial(squared_error_gradient, alpha = alpha),
															 x, y,
															 beta_intial,
															 0.001)										 

# шьраф лассо-регресии
def lasso_penalty(beta, alpha):
		return alpha * sum(abs.(beta_i) for beta_i in beta[1:])															 