import random


# сегментировать данные
def split_data(data, prob):
		# разбиение данных на части [prob, 1-prob]
		results = [], []
		for row in data:
				results[0 if random.random() < prob else 1].append(row)
		return results		

# разбиваем на конрольную и обучающую выборку
def tran_test_split(x, y, test_pct):	
		data = zip(x,y)															# обядинить соответствующие значения
		train, test = split_data(data, 1-test_pct)	# разбить список пар
		x_train, y_train = zip(*train)							# трюк с разьеденением списков
		x_test, y_test = zip(*test)	
		return x_train, y_train, x_test, y_test

# точность
def accuracy(tp, fp, fh, tn):
		currect = tp+ tn # правильный если истино положительный и истено отрецательный
		total = tp + fn + fp + tn 
		return currect / total	

# точность (как степень положительных значений прогнозов)
def precision(tp, fp, fh, tn):
		return tp / (tp / fp)		

# полнота
def recall(tp, fp, fh, tn):	
		return tp / (tp + fn)

# метрика F1
def f1_score(tp, fp, fh, tn):
		p = precision(tp, fp, fh, tn)
		r = recall(tp, fp, fh, tn)
		return 2 * p * r / (p + r)

