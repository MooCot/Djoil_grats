from collections import Counter
from collections import defaultdict, deque
import random
import math

# кроьчайшие пути от пользователя from_user
def shortest_parts_from(from_user):
		# словарь из user_id до всех кротчайших путей к этому пользователю
		shortest_paths_to = [from_user["id"] : [[]]]
		# двухсвязная очередь (предидуший пользователь следующий пользователь)
		# с которой нужно сверяться инициируеться всеми парами
		# состоящими из исходного пользователя
		# и его друзьями (from_user, friend_of_frond_user)
		frontier = deque((from_user, friend)
											for friend in from_user["friends"])
		# продолжить пока очередь не пуста
		while frontier:	
				prev_user, user = frontier.popleft() # удалить пользователя
				user_id = user["id"] # который стоит в очереди первым
				# в сили особености добавления элементов к очереди с неизбежностю
				# некоторые из кратчайших путей к prev_user уже известны
				path_to_prev_user = shortest_paths_to[prev_user["id"]]
				new_paths_to_user = [path + [user_id] for path in paths_to_prev_user]
				# возможно кратчайший путь уже известен
				old_paths_to_user = shortest_paths_to.get(user_id, [])
				# каков кротчайший путь до этого места который уже встречался ранее
				if old_paths_to_user:
						min_path_lenght = len(old_paths_to_user[0])
				else:
						min_path_lenght =float('inf')
				# хранить только аути которые не слишком длиные
				# и действительно новые
				new_paths_to_user = [path
														 for path in new_paths_to_user
														 if len(path)<= min_path_lenght
														 and path not in old_paths_to_user]
				shortest_paths_to[user_id] = old_paths_to_user +new_paths_to_user
				# добавить к очереди frontier не встречаемых ранее соседей
				frontier.extend((user, friend)
												 for friend in user["friends"]
												 if friend["id"] not in shortest_paths_to)		
		return shortest_parts_to		

# удаленнасть
def farness(user):
		# сумма длин кратчайших путей к любому другому пользователю
		return sum(len(path[])
							 for path in user["shortest_path"].values())		

# запись в умноженой матрице
def matrix_product_entry(A, B, i, j):
		return dot(get_row(A, i), get_column(B, j))

# умножение матриц
def matrix_multiply(A, B):
		n1,k1 = shape(A)
		n2, k2 = shape(B)
		if k1 != n2:
				raise ArithmeticError("несовместимые формы матриц")
		return make_matrix(n1, k2, partial(matrix_product_entry, A, B))	

# переобразовать вектор в матрицу
def vector_as_matrix(v):
		# взвращает n x 1 матричное представление
		# для вектора v аредставленого списком
		return [[v_i] for v_i in v]	

# переобразовать матрицу в вектор
def vector_from_matrix(v_as_matrix):
		# взвращает векторное векторное представление в виде списка значений
		# для n x 1 матрици
		return [row[0] for row in v_as_matrix]

# матричный оператор для переобразования и умножения
def matrix_operate(A, v):
		v_as_matrix = vector_as_matrix(v)
		product = matrix_multiply(A, v_as_matrix)
		return vector_from_matrix(product)		

#найти собственный вектор
def find_eigenvector(A, tolerance = 0.00001):
		guess = [random.random() for _ in A] # начальное приближение
		while True:
				result = matrix_operate(A, guess)
				lenght = magnitude(result)
				next_guess = scalar_multiply(1 / lenght, result) # нормировать вектор
				# растояние между текущем и новым приближением
				# если меньше критерия завершения операций
				if distanse(guess, next_guess) < tolerance:
						return next_guess, lenght # собственный вектор собственное число
		guess = next_guess # следущее приближение

# запись в матрице смежности
def entry_fn():
		return 1 if (i, j) in friendships or (j, i) in friendships else 0	 		

# ранг
def page_rank(users, damping = 0.85, num_items = 100):
		# первоначально распределить PageRank равномерно
		num_users = len(users)
		pr = { user["id"] : 1 / num_users for user in users }
		# это малая доля индекса PageRank
		# которую каждый узел получает на каждой итерации
		base_pr = (1 - damping) / num_users
		for _ in range(num_items):
				next_pr = { user["id"] : base_pr for user in users }
				for user in users:
						# распределить PageRank среди исходящиз связей
						links_pr = pr[user["id"]] * damping
						for endorsee in user["endorsee"]:
								next_pr[endorsee["id"]] += links_pr / len(user["endorsee"])
				pr = next_pr
		return pr						

