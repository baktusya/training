import math

masters_code = "Мастера кода"
wizards_data = "Волшебники данных"

#использование %
team1_num = input("Введите количество участников первой команды: ")
team2_num = input("Введите количество участников второй команды: ")

count1 = "В команде %s участников: %s!" % (masters_code, team1_num)
count2 = "В команде %s участников: %s!" % (wizards_data, team2_num)
teams = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)

#использование format()
score_1 = int(input("Введите количество задач решённых командой 1: "))
score_2 = int(input("Введите количество задач решённых командой 2: "))

result1 = "Команда {} решила задач: {}!".format(masters_code, score_1)
result2 = "Команда {} решила задач: {}!".format(wizards_data, score_2)

team1_time = float(input("Время за которое команда 1 решила задачи (в минутах): "))
team2_time = float(input("Время за которое команда 2 решила задачи (в минутах): "))

time_spent1 = "{} решили задачи за {} с !".format(masters_code, team1_time * 60)
time_spent2 = "{} решили задачи за {} с !".format(wizards_data, team2_time * 60)

#использование f-строк
total = f"Команды решили {score_1} и {score_2} задач"
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
summary = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {masters_code}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {wizards_data}!'
else:
    challenge_result = 'Ничья!'

print(count1, count2, teams, result1, result2, time_spent1, time_spent2, total, summary, challenge_result, sep='\n')

