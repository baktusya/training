def get_matrix(n, m, value):
    matrix = list()
    for i in range(n):
        stroka = list()
        for j in range(m):
            stroka.append(value)
        matrix.append(stroka)
    return matrix

example1 = get_matrix(2, 3, 7)
example2 = get_matrix(6, 2, 12)
example3 = get_matrix(5, 4, 8)
print(example1)
print(example2)
print(example3)
