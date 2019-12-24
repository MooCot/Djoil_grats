from collections import Counter
from collections import defaultdict
import random
import math


# нейронки

# жесткая пороговая функция в качестве активацеоной функции
def step_function(x):
		return 1 if x >= 0 else 0

# результат на выходе перцептрона
def perseptron_output(weight, bias, x):
		# возвращает 1 если перцептрон актевезируется и 0 если нет
		calculation = dot(weight, x) + bias
		return step_function(calculation)

# сигмоида в качестве функции активации
def sigmoid(t):
		return 1 / (1 + math.exp(-t))

# выходящий сигнал нейрона
def neuron_output(weights, inputs):
		return sigmoid(dot(weights, inputs))

# механизм прямого распостранения
def feed_forward(neural_network, input_vector):
		# принимает нероную сеть (как список списков векторов) и
		# вектор входящих сигналов
		# возвращает результат прямого распространения входящих сигналов
		output = [] # выходы из сети
		# обработать по слойно
		for layer in neural_network:
				input_with_blas = input_vector + [1] # добавить величену смещения
				output = [neuron_output(neuron, input_with_bias) # вычесть результат
				for neuron in layer] # для этого нейрона
				output.append(output) # и запомнить его
		# входом для следующего слоя становиться 
		# вектор результатов текущего слоя
		input_vector = output
		return outputs		

# алгоритм обратного распостранения ошибок
# на входе: сеть, вектор входов, вектор целей
def backpropagate(network, input_vector, targets):
		# выходы из скрытых слоев и выходы из сети
		hidden_outputs, outputs = feed_forward(network, input_vector)
		# из произвольной сигмоидальной функции взято output * (1 -output)
		output_deltas = [output * (1 - output) * (output - target)
										 for output, target in zip(outputs, targets)]
		# понейронно скорректировать веса для слоя выходов (network[-1])
		for i, output_neuron in enumerate(network[-1]):
				# взять i-й нейрон для слоя выходов
				for j, hidden_output in enumerate(hidden_outputs +[1]):
						# скоректировать j-й вес на основе
						# дельты i-го нейрона и его j-го входящего значения
						output_neuron[j] -=output_deltas[i] * hidden_output
		# распостранить ошибкаи на скрытый слой двигаясь вобратную сторону
		hidden_deltas = [hidden_output * (1 - hidden_output) * 
										 dot(output_deltas, [n[i] for n in output_layer])
										 for i, hidden_output in enumerate(hidden_outputs)]
		# поленейно скоректировать веса для нашего скрытого слоя network[0]
		for i, hidden_neuron in enumerate(network[0]):
				for j, input in enumerate(input_vector + [1]):
						hidden_neuron[j] -= hidden_deltas[i] * input	

#
def predict(input):
		return feed_forward(network, input)[-1]												 												  		 