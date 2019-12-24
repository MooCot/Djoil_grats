import gradient as gra
import random
from functools import partial
import vector as vec
import data_processing as pro
import Probability_theory as prob
from matplotlib import pyplot as plt 
import statistics as ind
import matrix as mat


# random.seed(0)

# uniform = [200 * random.random() -100 for _ in range(10000)]
# normal = [57 * prob.inverse_normal_cdf(random.random())
# 					for _ in range(10000)]
# pro.plot_histogram(uniform, 10, "Гистограма равномерных величин")
# pro.plot_histogram(normal, 10, "Гистограма нормальных величин")

#/////////////////////////////////////////////////////////////////

# xs = [pro.random_normal() for _ in range(1000)]
# ye1 = [x + pro.random_normal() / 2 for x in xs]		
# ye2 = [-x + pro.random_normal() / 2 for x in xs]		

# plt.scatter(xs, ye1, marker='.', color='black')
# plt.scatter(xs, ye2, marker='.', color='gray')
# plt.xlabel('xs')
# plt.ylabel('ys')
# plt.legend(loc=9)
# plt.title("очень разное совмесное распределение")
# plt.show()

# print(ind.correlation(xs, ye1)) # 0.9
# print(ind.correlation(xs, ye2)) # -0.9

#////////////////////////////////////////////////////////////////////////

# data = [[10, 10],
# 		[10, 20]
# 		]
# data = mat.make_matrix(5, 5, mat.is_diagonal)
# _, num_colums = mat.shape(data)

# fig, ax = plt.subplots(num_colums, num_colums)

# for i in range(num_colums):
# 		for j in range(num_colums):
# 				# разбросать столбец j по оси x напротив столбца i на оси Y
# 				if i != j: ax[i][j].scatter(mat.get_collumn(data, j), mat.get_collumn(data, i))
# 				# если не i == j показать имя серии 
# 				else: ax[i][j].annotate("серии "+ str(i), (0.5, 0.5),
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