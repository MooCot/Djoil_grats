from collections import Counter
from collections import defaultdict
import random
import math

# кластеризация

# класс выполняет кластеризацию по методу k средних
class KMeans:
		def __init__(self, k):
				self.k = k				 # число кластеров
				self.means = None	 # срднее кластеров

		def classify(self, imput):
				# вернуть индекс кластеров ближайшего к входящему значению input
				return min(range(self.k),
													key=lambda i: squared_distance(input, self.means[i]))

		def train(self, inputs):
				# выбрать k случайных точек в качестве исходных средних
				self.means = random.sample(imputs, self.k)
				assignments = None
				while True:
						# найти новые назначения
						new_assignments = map(self.classify, inputs)
						# если ни одно назначение не изменилось то завершить
						if assignments == new_assignments:
								return
						# в противном случае сохранить новые назначения
						assignments = new_assignments
						# и вычеслить новые средние на основе новых назначений
						for i in range(self.k):
								# найти все точки назначеные кластеру i
								i_points = [p for p, a in zip(inputs, assignments) if a == i]
								# удостовериться что i_points не пуст чтобы не делить на 0
								if i_points:
										self.means[i] = vector_mean(i_points)															

# сумарное квадратичное отклонение кластеризации
def squared_clustering_errors(inputs, k):
		# находит сумарное квадратичное отлонение(ошибку)
		# от k средних до кластеризации входящих данных
		clusterer = KMeans(k)
		clusterer.train(inputs)
		means = clusterer.means
		assignments = map(clusterer.classify, inputs)
		return sum(squared_distance(input, means[cluster])
							 for input, cluster in zip(inputs, assignments))	
							 
def recolor(pixel):
		cluster = clusterer.classify(pixel) # индекс ближайшего кластера
		return clusterer.means[cluster]			#	среднее ближайшего кластера

# проверка на лист кластер
def is_leaf(cluster):	
		# кластер еться лист если длин == 1
		return len(cluster) == 1				 	

# получить дочерные элементы
def get_children(cluster):
		# вернуть 2 дочерних элемента данного кластера
		# еслт он обьедененный кластер, вызывает исключение
		# если это лист кластер
		if is_leaf(cluster):
				raise TypeError("листовой кластер не имеет дочерных элементов")
		else:
				return cluster[1]

# получить значения
def get_values(cluster):
		# вернуть значения в кластере (если лист кластер)
		# или все значения в листовых кластерах под ним
		if is_leaf(cluster):
				return cluster		# это одноэлементный кортеж содержащий значение
		else:
				return [value
								for child in get_children(cluster)
								for value in get_values(child)]		

# растояние между двумя кластерами
def cluster_distance(cluster1, cluster2, distance_agg=min):
		# вычеслить все попарные растояния между cluster1 cluster2
		# и применить функцию обьединения _distance_agg_
		# к результуещему списку
		return distance_agg([distance(input1, input2)
												for input1 in get_values(cluster1)
												for input2 in get_values(cluster2)])

# получить порядковый номер обьядинения
def get_merge_order(cluster):
		if is_leaf(cluster):
				return float('int')
		else:										# порядковый номер merge_order 
				return cluster[0]		#	это 1-й элемент 2-элементарного кортежа

# восходящий (снизу вверх) алгоритм кластеризации
def boottom_up_cluster(inputs, distance_agg=min):
		# начать с ього что все входы листовые кластеры / 1 - элемент кортеж
		clusters[(input,) for input in inputs]
		# пока останеться более одного кластера
		while len(clusters) > 1:
				# найти 2 ближайших кластера
				c1, c2 = min([(cluster1, cluster2)
											 for i, cluster1 in enumerate(clusters)
											 for cluster2 in clusters[:i]],
											 key=lambda (x, y): cluster_distance(x, y, distance_agg))
				# исключить их из списка кластеров
				clusters = [c for c in clusters if c != c1 and c !=c2]
				# обядинить их использя переменую порядкового номера
				# обьяедиенние merged_order = число оставшихся кластеров
				merged_cluster = (len(clusters), [c1, c2])
				# и добавить их обьединение к списку кластеров
				clusters.append(merged_cluster)	
				# когда останеться 1 кластер вернуть его
				return clusters[0]	

# сгенерировать кластер
def generate_clusters(base_cluster, num_clusters):	
		# начать со списка. состоящего только из базового кластера
		clustes = [base_cluster]
		# продолжить пока кластеров не достаточно
		while len(clustes) < num_clusters:
				# выбрать из списка тот который был обьединен последним
				next_cluster = min(clustes, key=get_merge_order)
				# исключить его из списка
				clusters = [c for c in clusters if c !=next_cluster]
				# и добавить его дочерные элементы к сприску
				# (ч. е. разьединить его)
				clusters.extend(get_children(next_cluster))
		# когда уже достаточно кластеров
		return clusters										 
