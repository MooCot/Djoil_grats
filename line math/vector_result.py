import matrix
import vector

height_weight_age = [2, 3]
grades = [1, 2]
scalar = 2
A = [[1, 2],
		[1, 2],
		[1, 2]]

складывает векторы 
result_vec_add = vector.vector_add(height_weight_age, grades)
print(result_vec_add)

# вычетает векторы 
result_vec_sub = vector.vector_subtract(height_weight_age, grades)
print(result_vec_sub)

# покомпонентная сума списка векторов
result_vec_sum = vector.vector_sum(A)
print(result_vec_sum)

# умножение вектора на скаляр
result_vec_dist = vector.scalar_multiply(scalar, grades)
print(result_vec_dist)

# покомпонентное среднее значение списка векторов
result_vec_mean = vector.vector_mean(A)
print(result_vec_mean)

# скалярное произведение
result_dot = vector.dot(height_weight_age, grades)
print(result_dot)

# сумма квадратов вектора
result_sum_of_squares = vector.sum_of_squares(grades)
print(result_sum_of_squares)

# длина вектора
result_magnitude = vector.magnitude(grades)
print(result_magnitude)

# квадрат растояния между двумя векторами
result_squared_distance = vector.squared_distance(grades, height_weight_age)
print(result_squared_distance)

# растояние между двумя векторами
result_distance = vector.distance(grades, height_weight_age)
print(result_distance)

