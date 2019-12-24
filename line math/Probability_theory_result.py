import Probability_theory as prob
from collections import Counter
import math
from matplotlib import pyplot as plt 

x = 2
y = 3

# ДНФ равномерного распределения
# result_uniform_pdf = prob.uniform_pdf(x)
# print(result_uniform_pdf)

# ИФР равномерного распределения
# result_uniform_cdf = prob.uniform_cdf(x)
# print(result_uniform_cdf)

# ДФР нормального распределения
# result_normal_pdf = prob.normal_pdf(x)
# print(result_normal_pdf)

# ИФР нормального распределения
# result_normal_cdf= prob.normal_cdf(x)
# print(result_normal_cdf)

# обратная ИФР нормального распределения
# result_inverse_normal_cdf = prob.inverse_normal_cdf(x)
# print(result_inverse_normal_cdf)

# независимое испытание бернули
# result_bernoulli_trial = prob.bernoulli_trial(x)
# print(result_bernoulli_trial)

# биномиальное распределение
# result_binomial = prob.binomial(x,y)
# print(result_binomial)

# биномиальное распределение
# result_binomial = prob.binomial(x,y)
# print(result_binomial)

# def make_hist(p, n, num_points):
# 		data = [prob.binomial(n, p) for _ in range(num_points)]
		
# 		# Столбчастая диограма показивающая биномиальные выборки
# 		histogram = Counter(data)
# 		plt.bar([x - 0.5 for x in histogram.keys()],
# 						[v / num_points for v in histogram.values()],
# 						0.8,
# 						color = '0.75')
# 		mu = p * n
# 		sigma = math.sqrt(n * p *(1 - p))
		
# 		# линейный график показывающий нормальное разпределение
# 		xs = range(min(data), max(data) + 1)
# 		ys = [prob.normal_cdf(i + 0.5, mu, sigma) - prob.normal_cdf(i - 0.5, mu, sigma)
# 				 for i in xs]
# 		plt.plot(xs, ys)
# 		plt.title("Биноминальное распределение и его нормальное приближение")
# 		plt.show()

# make_hist(0.75, 100, 10000)		


# биномиальное распределение
# result_normal_approximation_to_binomial = prob.normal_approximation_to_binomial(1,1)
# print(result_normal_approximation_to_binomial)


# result_normal_probability_above = prob.normal_probability_above(1)
# print(result_normal_probability_above)

# result_normal_probability_between = prob.normal_probability_between(1, 2)
# print(result_normal_probability_between)

# result_normal_probability_outside = prob.normal_probability_outside(1, 2)
# print(result_normal_probability_outside)

# верхняя граница нормальной велечены
# result_normal_upper_bound = prob.normal_upper_bound(2)
# print(result_normal_upper_bound)

# нижняя граница нормальной велечены
# result_normal_lower_bound = prob.normal_lower_bound(2)
# print(result_normal_lower_bound)

# двухстороняя граница нормальной велечены
# result_normal_two_sided_bound = prob.normal_two_sided_bound(2)
# print(result_normal_two_sided_bound)

# двух сторонее p значение
# result_two_sided_p_value = prob.two_sided_p_value(2)
# print(result_two_sided_p_value)

# оценочные параметры
# result_estimated_parametes = prob.estimated_parametes(2, 2)
# print(result_estimated_parametes)

# статистика a/b тестирования
# result_a_b_test_statistic = prob.a_b_test_statistic(1000, 200, 1000, 180)
# print(result_a_b_test_statistic)

# нормализация
# result_B = prob.B(50, 50)
# print(result_B)

# ДФР для бета распределений случайной величины
# result_beta_pdf = prob.beta_pdf(0.5, 40, 60)
# print(result_beta_pdf)

