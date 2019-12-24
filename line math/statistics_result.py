import statistics as stat
from collections import Counter
from matplotlib import pyplot as plt 
import vector

num_friends = [
	100,3 ,34,12,43,65,23,43,1,
	43,23,54,23,34,45,23,54,23,
	5,12,23,21,43,12,24,54,23,23,
	54,32,34,54,65,65,67,34,56,12,
	43,21,23,45,65,67,23,43,65,
	23,54,4,6,8,2,6,8,5,8,9,5,3,4,6,
	12,14,5,11,14,5,3,5,13,15,14,18, 
	45, 24,26, 30,31,35,36,37,40,41,49,
	50,51,52,53,54,47,48,49,57,58,57,58,
	59,60,61,61,63,63,64,12,15,16,17
]

minutes = [1, 170, 205, 120, 220, 130, 105, 145, 190, 120,
					110,20,180,70,10,100,170,140,130,110,150,160,
					170,180,120,110,150,40,50,160,220,320,310,340,
					340,360,120,220,120,150,170,130,140,220,250,90,
					250,120,190,120,120,120,120,145,120,130,120,120,
					120,190,130,120,145,120,120,130,120,120,120,145,
					130,120,120,120,250,145,120,250,190,120,190,120,
					145,120,120,120,130,120,120,130,120,120,120,120,
					120,250,120,120,190,120,145,120,120,120,120,250,
					120,250]

# friend_counts = Counter(num_friends)
# xs = range(101)
# ys = [friend_counts[x] for x in xs]
# plt.bar(xs, ys)
# plt.axis([0, 120, 0, 30])
# plt.title("гистограма количества друзей")
# plt.xlabel("Количество друзей")
# plt.ylabel("Количество людей")
# plt.show()

# num_points = len(num_friends)
# largest_value = max(num_friends)
# smallest_value = min(num_friends)
# sorted_values = sorted(num_friends)
# smallest_value = sorted_values[0]
# largest_value = sorted_values[-1]

# среднее значение
# result_mean = stat.mean(num_friends)
# print(result_mean)

# медиана
# result_median = stat.median(num_friends)
# print(result_median)

# квантиль mode
# result_quantile = stat.quantile(num_friends, 0.70)
# print(result_quantile)

# мода
# result_mode = stat.mode(num_friends)
# print(result_mode)

# показатели вариации
# result_data_range = stat.data_range(num_friends)
# print(result_data_range)

# измеряет отклонение одной переменной от ее среднего 
# result_de_mean = stat.de_mean(num_friends)
# print(result_de_mean)

# измеряет отклонение одной переменной от ее среднего 
# result_variance = stat.variance(num_friends)
# print(result_variance)

# стандартное отклонение для дисперсии
# result_standart_deviations = stat.standart_deviations(num_friends)
# print(result_standart_deviations)

# интерактивный размах
# result_interquartile_range = stat.interquartile_range(num_friends)
# print(result_interquartile_range)

# ковариация
# result_covariance = stat.covariance(num_friends, minutes)
# print(result_covariance)

# корреляция
# result_correlation = stat.correlation(num_friends, minutes)
# print(result_correlation)

# отфильтровать выброс
# num_friends_good = [x
# 									 for i, x in enumerate(num_friends)
# 									 if i != outlier]

# minutes_good = [x
# 								for i, x in enumerate(minutes)
# 								if i != outlier]

# print(stat.correlation(num_friends_good, minutes_good))								
