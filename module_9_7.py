def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 1:
            pass
        for div in range(2, result // 2 + 1):
            if result % div == 0:
                print('Составное')
                break
        else:
            print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
result2 = sum_three(4, 8, 6)
print(result2)