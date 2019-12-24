import math
import random

# ДНФ равномерного распределения
def uniform_pdf(x):
		return 1 if x >= 0 and x < 1 else 0

# ИФР равномерного распределения
def uniform_cdf(x):
		if x<0: return 0
		elif x<1: return x 
		else: return 1

# # ДФР нормального распределения
def normal_pdf(x, mu=0, sigma=1):
		sqrt_two_pi = math.sqrt(2 * math.pi)
		return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / sqrt_two_pi * sigma)

# # ИФР нормального распределения
def normal_cdf(x, mu=0, sigma=1):
		return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# # обратная ИФР нормального распределения
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance = 0.00001):
		if mu != 0 or sigma != 1:
				return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)
		low_z, low_p = -10.0, 0
		hi_z, hi_p = 10.0, 0
		while hi_z - low_z > tolerance:
				mid_z = (low_z + hi_z) / 2
				mid_p = normal_cdf(mid_z)
				if mid_p < p:
						low_z, low_p = mid_z, mid_p
				elif mid_p > p :
						hi_z, hi_p = mid_z, mid_p
				else:
						break
		return mid_z							

# # независимое испытание бернули. в котором имеется только 2 случайных исхода
# # (1, 0) с постояной вероятностю
def bernoulli_trial(p):
		return 1 if random.random() < p else 0

# # биномиальное распределение
def binomial(n, p):
		return sum(bernoulli_trial(p) for _ in range(n))

# #////////////////////////////////////////////////////
# # # апроксимация биноминальной случайной величины нормальным распределением
def normal_approximation_to_binomial(n, p):
		""" находит mu и сигма каторые соответствуют binomial(n, p) """
		mu = p * n
		sigma = math.sqrt(p * (1 - p) * n)
		return mu, sigma

# # вероятность что значение нормальной случайной величины лежит
# # ниже порогового значения 
normal_probability_below = normal_cdf

# # выше порогового значения, если оно не ниже порогового значения 
def normal_probability_above(lo, mu=0, sigma=1):
		return 1 - normal_cdf(lo, mu, sigma)

# # оно лежит между если оно не меньше hi но не ниже lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
		return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# # оно лежит за пределами если оно не внутри
def normal_probability_outside(lo, hi, mu=0, sigma=1):
		return 1 - normal_probability_between(lo, hi,mu, sigma)

# # верхняя граница нормальной велечены
def normal_upper_bound(probability, mu=0, sigma=1):
		# возвращает z для которого P(Z<=z) = probability
		return inverse_normal_cdf(probability, mu, sigma)		

# # нижняя граница нормальной велечены
def normal_lower_bound(probability, mu=0, sigma=1):
		# возвращает z для которого P(Z>=z) = probability
		return inverse_normal_cdf(1 - probability, mu, sigma)	

# # двухстороняя граница нормальной велечены
def normal_two_sided_bound(probability, mu=0, sigma=1):
		# возвращает симетричные (вокруг среднего значения) границы в пределах которых содержиться указаная вероятоность
		tail_probapility = (1 - probability) / 2		
		# верхняя граница должна иметь значение 
		# tail_probapility выше ее
		upper_bound = normal_lower_bound(tail_probapility, mu, sigma)	
		# верхняя граница должна иметь значение 
		# tail_probapility ниже ее
		lower_bound = normal_upper_bound(tail_probapility, mu, sigma)
		return lower_bound, upper_bound

# #///////////////////////////////////////////////////////////////////////
# # P- значения

# # двух сторонее p значение
def two_sided_p_value(x, mu=0, sigma=1):
		if x >= mu:
				# если х больше среднего значения. то значение в хвосте больше х
				return 2 * normal_probability_above(x, mu, sigma)
		else:	
				# если х меньше среднего значения. то значение в хвосте меньше х
				return 2 * normal_probability_below(x, mu, sigma)	

upper_p_value = normal_probability_above # верхнее p значение
below_p_value = normal_probability_below # нижнее p значение

# # оценочные параметры
def estimated_parametes(N, n):
		p = n / N
		sigma = math.sqrt(p * (1 - p) / N)
		return p, sigma

# # статистика a/b тестирования
def a_b_test_statistic(N_A, n_A, N_B, n_B):
		p_A, sigma_A = estimated_parametes(N_A, n_A)
		p_B, sigma_B = estimated_parametes(N_B, n_B)
		return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

# #////////////////////////////////////////////////////////////////////////
# # бейсовский статистический вывод		

# # нормализация
def B(alpha, beta):
		return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

# # ДФР для бета распределений случайной величины
def beta_pdf(x, alpha, beta):
		if x < 0 or x > 1:
				return 0 
		return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta) 			