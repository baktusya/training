from multiprocessing import Pool
from time import time


def read_info(name):
    all_data = list()

    with open(name, 'r') as file:
        for readline in file :
            all_data.append(readline.strip())
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time()
read_info(r'C:\Users\Пользователь\PycharmProjects\training\Files\file 1.txt')
end_time = time()
time_spent = end_time - start_time
print(time_spent, '(линейный по абсолютному пути)')

start_time = time()
read_info('file 2.txt')
end_time = time()
time_spent = end_time - start_time
print(time_spent, '(линейный)')


start_time = time()
read_info('file 3.txt')
end_time = time()
time_spent = end_time - start_time
print(time_spent, '(линейный)')

start_time = time()
read_info('file 4.txt')
end_time = time()
time_spent = end_time - start_time
print(time_spent, '(линейный)')


# Многопроцессный
# start_time = time()
# if __name__ == '__main__':
#     with Pool(processes=4) as p:
#         p.map(read_info, filenames)
#         p.close()
#         p.join()
#     end_time = time()
#     time_spent = end_time - start_time
#     print(time_spent, '(многопроцессорный)')
