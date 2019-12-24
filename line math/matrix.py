# возвращает кол строк, и колонок
def shape(A):
		num_rows = len(A)
		num_cols = len(A[0]) if A else 0
		return num_cols, num_rows

# получить i-ю строку
def get_row(A, i):
		return A[i]

# получить j-ю столбец
def get_collumn(A, j):
		return[A_i[j]
					for A_i in A]

def make_matrix(num_cols, num_rows, entry_fn):
		''' возвращает матрицу размера num_rows*num_cols, 
		(i, j)-й элемент который равен функции entry_fn(i, j) '''
		return [[entry_fn(i, j)
					 for j in range(num_cols)]
					 for i in range(num_rows)]

# 1 по диагонале остальное все 0
def is_diagonal(i, j):
		return 1 if i==j else 0