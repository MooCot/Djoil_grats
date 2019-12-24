from collections import Counter
from collections import defaultdict
import random
import math

# обработка естественого языка

# размер текста
def text_size(total):
		# равно 8 если total = 0, 29, 200
		return 8 + total / 200 * 20

def fix_unicode(text):
		return text.replace(u"\u2019", ",")

# сгенерировать при помощи биграм
def generate_using_bigrams():
		current = "." # означает что следующее слово начинает предложение
		result = []
		while True:
				next_word_candidates = transitions[current] 	# бигграмы (current, _)
				current = random.choice(next_word_candidates)	# выбрать произвольно
				result.append(current)												# добавить к результатам
				if current == ".": return " ".join(result)		# если ".", то закончить

# сгенерировать при помощи триграм
def generate_using_trigrams():
		current = random.choice(starts) # если предедущее слово точка
		prev = "."											# то это слово исходное
		result =[current]
		while True:
				next_word_candidates = trigram_transitions[(prev, current)]
				next_word = random.choice(next_word_candidates)
				prev, current = current, next_word, result.append(current)
				if current == ".":
						return " ".join(result)

# это терминал
def is_terminal(token):
		return token[0] != "_"

# расширить лексемы (применить правила подстановки) при заданной граматике
def expend(grammar, tokens):
		for i, token in enumerate(tokens):
				# пропустить терминалы
				if is_terminal(token): continue
				# если мы тут значит нашли нетерминальную лексему
				# произвольно выбрать для нее подстановку
				replacement = random.choice(grammar[token])
				if is_terminal(replacement):
						tokens[i] =replacement
				else:
						token = tokens[:i] + replacement.split() + tokens[(i+1):]
				# теперь вызвать функцию eexpend с новым списком лекслем
				return expend(grammar, tokens)
		# имеем одни терминалы закончить работу
		return tokens					

# сгенерировать предложение с заданой граматикой
def generate_sentence(grammar):		
		return expend(grammar, ["_S"])

# бросить кубик
def roll_a_die():
		return random.choice([1,2,3,4,5,6])

# бросить кубик
def direct_sample():
		d1 = roll_a_die()
		d2 = roll_a_die()
		return d1, d2 + d1

# случайное y в зависимости от x
def random_y_given_x(x):
		# равновероятное значение будет x+1, x+2 ... x+6
		return x + roll_a_die()		

# случайное x в зависимости от y
def random_x_given_y(y):
		if y <=7:
				# если сумма <= 7 первый кубик равновероятно будет равен
				# 1, 2 3 4 5 6, сума - 1
				return random.randrange(1, y)
		else:
				# если сумма <= 7 первый кубик равновероятно будет равен
				# сумаа -6 , сумаа -5 ....
				return random.randrange(y - 6,7)		

# выборка по гибсону
def gibbs_sample(num_items=100):
		x, y =1, 2 # пох на числа. ранд
		for _ in range(num_items): 
				x = random_x_given_y(y) # случайное x в зависимости от y
				y = random_y_given_x(x) # случайное y в зависимости от x
		return x, y		

# сравнить распределения
def compare_distributions(num_samples=100):
		counts = defaultdict(lambda: [0, 0])
		for _ in range(num_samples):
				counts[gibbs_sample()][0] +=1
				counts[direct_sample()][0] +=1
		return counts		

# случайная выборка индекса из множества (весов)
def sample_from(weights):
		# возвращает i с вероятностю по формуле weights[i] / sum(weights)
		total = sum(weights)
		rnd = total * random.random() # равномерно между 0 и суммой
		for i, w in enumerate(weights):
				rnd -=w # веруть найменьшый i такой что
				if rnd <=0: return i # weights[0] +...+weights[i]>= rnd

# вероятность тематики в зависимости от документа
def p_topic_given_document(topic, d, alpha = 0.1):
		# доля слов в документе _d_ которые
		# назначаются тематике _topic_ 
		return((document_topic_counts[d][topic] + alpha) /
						(document_lenghts[d] + K * alpha))

# вероятность слова в зависимости от тематики
def p_word_given_topic(word, topic, beta = 0.1):
		# доля слов назначаемых тематике _topic_, которые равны _word_ 
		return ((topic_word_counts[topic][word] + beta) /
						 (topic_counts[topic] + W * beta))

# вес тиматики
def topic_weight(d, word, k):
		# приналичии документа и слова в этом документе
		# вернуть вес k-темы
		return p_word_given_topic(word, k) * p_topic_given_document(k, d)

# выбрать новую тематику
def choice_new_topic(d, word):
		return sample_from([topic_weight(d, word, k)
												for k in range(K)])		
		
