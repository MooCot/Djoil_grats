from collections import Counter
import math
import vector as vec
#///////////////////////////////////////////////////////
# показатели центра распределения
# среднее значение
def mean(x):
		return sum(x) / len(x)

# если список не четный (x 5 эл) то берется x[2]
# четный то ,берется среднее зн x[2] и x[3]
def median(v):
		n = len(v)
		sorted_v = sorted(v)
		midpoint = n // 2

		if n % 2:
				return sorted_v[midpoint]		
		else:
				lo = midpoint - 1
				hi = midpoint
				return (sorted_v[lo] + sorted_v[hi]) / 2		

# квантиль
# возврашает значение меньше p%  
def quantile(x, p):
		p_index = int(p * len(x))	
		return sorted (x)[p_index]

# мода наиболее часто встречаемое значение
def mode(x):
		counts = Counter(x)
		max_count = max(counts.values())
		return [x_i for x_i, count in counts.items()
						if count == max_count]

#/////////////////////////////////////////////
# показатели вариации
# диапазон (разница мин - макс зн)
def data_range(x):
		return max(x) - min(x)

# дисперсия-
# измеряет отклонение одной переменной от ее среднего 
def de_mean(x):
		# пересчитать х, вычнтя его среднее
		x_bar = mean(x)
		return [x_i - x_bar for x_i in x]

# дисперсия - это средняя сума квадратов отклонения от среднего
def variance(x):
		n = len(x)
		deviations = de_mean(x)
		return vec.sum_of_squares(deviations) / (n - 1)

# стандартное отклонение для дисперсии так как дисперсия **2
def standart_deviations(x):
		return math.sqrt(variance(x))

# интерактивный размах
# позволяет посмотреть разницу между 25% и 75%
def interquartile_range(x):
		return quantile(x, 0.75) - quantile(x, 0.25)		

# ковариация 
# измеряет отклонение 2 переменных от своих среднего
def covariance(x, y):
		n=len(x)
		return vec.dot(de_mean(x), de_mean(y)) / (n - 1)


# корреляция
# кавариляция распределяеться между стандартными отклонениями обеих переменных
# ответ от -1 нет(атикор) до 1 влияет(кор)
def correlation(x, y):
		stdev_x = standart_deviations(x)
		stdev_y = standart_deviations(y)
		if stdev_x > 0 and stdev_y > 0:
				return covariance(x, y) / stdev_x / stdev_y
		else:
				return 0		
