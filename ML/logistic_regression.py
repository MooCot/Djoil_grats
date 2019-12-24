import random
import math

# логистическая регресия

# логистическа функция
def logistic(x):
		return 1.0 / (1 + math.exp(-x))

# первая производная логистической функции (штрих)
def logistic_prime(x):
		return logistic(x) * (1 - logistic(x))

# логарифмическая функция подобия для данных с индексом i
def logistic_log_likehood_i(x_i, y_i, beta):
		if y_i == 1:
				return math.log(logistic(dot(x_i, beta)))
		else:
				return math.log(1 - logistic(dot(x_i, beta)))			

# логарифмическое правдопадобие
def logistic_log_likehood(x, y , beta):
		return sum(logistic_log_likehood_i(x_i, y_i, beta)
							for x_i, y_i in zip(x, y))		

# частная по ij
def logistic_log_partial_ij(x_i, y_i, beta, j):
		# здесь i индекс точки данных j индекс производной
		return (y_i - logistic(dot(x_i, beta))) * x_i[j]			

# градиент по i
def logistic_log_gradient_i(x_i, y_i, beta):
		# градиент логарифмической функции правдоподобия
		# соответствующий i-й точке данных
		return [logistic_log_partial_ij(x_i, y_i, beta, j)
					 for j, _ in enumerate(beta)]	

# градиент
def logistic_log_gradient(x, y , beta):		
		return reduce(vector_add,
								 [logistic_log_gradient_i(x_i, y_i, beta)
								 for x_i, y_i in zip(x, y)])			 								