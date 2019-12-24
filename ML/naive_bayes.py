from collections import Counter
import random


# спам фильтр


# сгенерировать список слов без повторов
def tokinize(message):
		message = message.lower()										 # переобразовать в строчные
		all_words = re.findall("[a-z0-9]+", message) # извлеч слова
		return set(all_words)												 # удалить повторы

# подсчитать частотность слов
def count_words(training_set):
		# обучающая выборка состоит из пар (сообщение. спам)
		counts = defaltdict(lambda: [0,0])
		for message, is_spam in training_set:
				for message, is_spam in training_set:
						counts[word][0 if is_spam else 1] +=1
		return counts				

# вероятности слов
def word_propabilities(counts, total_spams, total_non_spams, k=0.5):
		# переобразовать частотности word_counts в список триплетов
		# слово w, p(w ! spam) и p(w ! ~spam)
		return[(w,
					(spam + k) / (total_spams + 2 *k),
					(non_spam + k) / (total_non_spams + 2 * k))
					for w, (spam, non_spam) in counts.items()]		

# вероятность спама
def spam_probability(word_probs, message):			
		message_words = tokinize(message)
		log_prob_if_spam = log_prob_if_not_spam = 0.0
		# просмотреть все слова в словаре 
		for word, prob_if_spam, prob_if_not_spam in word_probs:
				# если слово появляеться в сообщении
				# то добавить лог вероятность встретить его в сообщении
				if word in message_words:
						log_prob_if_spam+=math.log(prob_if_spam)
						log_prob_if_not_spam+=math.log(prob_if_not_spam)
				# если слово не появляеться в сообщении
				# то добавить лог вероятность не встретить его в сообщении
				# вычесляемое его как log(1 - вероятность его встретить)
				else:
						log_prob_if_spam+=math.log(1.0 - prob_if_spam)
						log_prob_if_not_spam+=math.log(1.0 - prob_if_not_spam)
		prob_if_spam = math.exp(log_prob_if_spam)
		prob_if_not_spam = math.exp(log_prob_if_not_spam)
		return prob_if_spam / (prob_if_spam + prob_if_not_spam)

# спам фильтр
class NaiveBayesClass:
		
		def __init__(self, k=0.5):
				self.k=k
				self.word_probs=[]
		# обучить класофикатор при помощи обучающей выборки
		def train(self, training_set):
				# подсчитать спамные и не спамные сообщения
				num_spams = len([
												for message, is_spam in training_set
												if is_spam])
				num_non_spams = len(training_set) - num_spams
				# пропустить обучающюю выборку через конвейр
				word_counts = count_words(training_set)
				self.word_probs = word_propabilities(word_counts,
																						num_spams,
																						num_non_spams,
																						self.k)
				def classify(self, message):
						return spam_probability(self.word_probs, message)																		
