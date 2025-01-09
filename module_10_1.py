from time import sleep, time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            string = f'Какое-то слово № {i}'
            file.write(string + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

'''вызов функций и подсчёт времени'''
start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f'Время выполнения функций: {end_time - start_time} секунд')

start_time_flow = time()
threads = list()   #создание пустого списка потоков

'''cоздание потоков'''
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

'''запись потоков в список'''
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

'''запуск потоков'''
for thread in threads:
    thread.start()

'''ожидание завершения всех потоков'''
for thread in threads:
    thread.join()

end_time_flow = time()
print(f'Работа потоков {end_time_flow - start_time_flow} секунд')