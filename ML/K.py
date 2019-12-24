from collections import Counter
import random

# грубый подсчет большенства голосов
def raw_majority_vote(labels):
		votes = Counter(labels)
		winner, _ =votes.most_common(1)[0]
		return winner

# оьбор по большенству голосов
def majority_vote(labels):
		# подразумевает что метки упорядочены от ближайшей
		# до самой удаленной
		vote_counts = Counter(labels)
		winner, winner_count = vote_counts.most_common(1)[0]
		num_winners = len([
											count
											for count in vote_counts.values()
											if count == winner_count])

		if num_winners == 1:
				return winner # единственный победитель поетому вернуть его
		else:
				return majority_vote(labels[:-1]) # попытаться снова
																					#	без смого дального

# клссыфицировать на основе k ближайших соседей
def knn_classify(k, labaled_points, new_point):
		# каждая маркированая точка должна быть представлена 
		# парой (точка. метка)
		# упорядочить маркированые точки от ближайшей до самой удаленной
		by_distance =sorted(labaled_points,
												key=lambda (point, _): distance(point, new_point))
		# найти метки для k ближайших
		k_nearest_labels = [label for _, label in by_distance[:k]]
		# и дать им проголосовать
		return majority_vote(k_nearest_labels)										

#//////////////////////////////////////////////////////////////////
# проблема размерности

# генерирование случайных точек
def random_point(dim):
		return [random.random() for _ in range(dim)]

# генерирование случайных растояний
def random_distances(dim, num_points):
		return [distance(random_point(dim), random_point(dim))
					 for _ in range(num_points)]		