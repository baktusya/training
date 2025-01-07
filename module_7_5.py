import os

directory = r'C:\Users\Пользователь\PycharmProjects\training'
for i in os.walk(directory):
    print(i)
