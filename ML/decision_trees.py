from collections import Counter
from collections import defaultdict
import random
import math

# деревья принятия решений

# энтрпия
def entropy(class_probailities):
		# при заданом списке вероятностей классов вычеслить энтропию
		return sum(-p * math.log(p, 2)
							for p in class_probailities
							if p)												# игнорирование 0 вероятности

# вероятности классов
def class_probailities(labels):
		total_count = len(labels)  # сумарное число
		return [count / total_count
					 for count in Counter(labels).values()]

# энтропия маркировочных данных
def data_entropy(labeled_data):
		labels = [label for _ ,label in labeled_data]
		probabilities = class_probailities(labels)
		return entropy(probabilities)

# энтропия розбиения для подмножества
def partition_entropy(subsets):
		# найти энтропию исходя из этого разбиения данных на подгрупы
		# подгруппы представляют собой список списков маркированых данных
		total_count = sum(len(subset) * len(subset) / total_count
										 for subset in subsets)		

# разбить входящие данные по атрибуту
def partition_by(inputs, attribute):
		# каждый элемент в inputs представляет собой пару 
		# (словарь attribute_dict, метка label)
		# возвращает словарь dict
		# где ключ атрибутта attribute_value значение = inputs
		groupts = defaultdict(list)
		for input in inputs:
				key = input[0][attribute]  # взять значение атрибута и добавить
				groupts[key].append(input) # входящюю пару к соответствующему списку
		return groupts												 

# энтропия разбиения по атрибуту
def partition_entropy_by(inputs, attribute):
		# вычесляет энтропию соответствющую заданому разбиению
		partitions = partition_by(inputs, attribute)
		return partition_entropy(partitions.values())

# классифицировать входящие значения, используя заданое дерево ДПР
def classify(tree, input):
		# если это листовой узел вернуть его заначение
		if tree in [True, False]:
				return tree		
		# иначе дерево состоит из атрибута, по которому пройдет расщепление
		# и словаря где ключи это значения этого атрибута а
		# значения это поддеревья подлежащие рассмотрению в следующию очередь
		attribute, subtree_dict = tree
		subtree_key = input.get(attribute) # None если на входе отсутствует атрибут
		if subtree_key not in subtree_dict # если для ключа нет поддерева
				subtree_key = None
		subtree = subtree_dict[subtree_key] # выбрать соответствующие поддерево
		return classify(subtree, input)     #	и использовать для классыфикации					

# построить дерево на основе алгоритма id3
def build_tree_id3(inputs, split_candidats = None)
		# если это первый проход то
		# все ключи первоначальных входящих данных - это выделенные претенденты
		if split_candidats is None:
				split_candidats = inputs[0][0]
		# подсчитать число True и False во входящих значениях
		num_inputs = len(inputs)
		num_trues = len([label for item, label in inputs if label])
		num_falses = num_inputs - num_tues
		if num_trues == 0: return False # если True отсутствует вернуть лист False
		if num_falses == 0: return True # если False отсутствует вернуть лист True
		if not split_candidats:          # если нет кандидатов 
				return num_trues >=num_falses	#	вернуть лист большенства

		#	в противном случае выполнить расщепление по лучшему фтрибуту	
		best_attribute =min(split_candidats,
												key=partial(partition_entropy_by, inputs))
		
		partitions = partition_by(inputs, best_attribute)
		new_candidates = [a for a in split_candidats
										 if a != best_attribute]

		# рекурсивно созать деревья
		subtrees = { attribute_value : build_tree_id3(subset, new_candidates)
											for attribute_value, subset in partitions.item()}
		subtrees[None] = num_trues > num_falses # случай по умолчанию
		return (best_attribute, subtrees)		

# классифицировать на основе лесса
def forest_classify(trees, input):
		votes = [classify(trees, input) for tree in trees]
		vote_counts = Counter(votes)
		return vote_counts.most_common(1)[0][0]											