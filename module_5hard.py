import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname                        #имя пользователя
        self.password = self._hash_password(password)   #пароль
        self.age = age                                  #возраст

    def _hash_password(self, password):
        return int(hash(password))

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = str(title)         #заголовок
        self.duration = duration        #продолжительность
        self.time_now = 0               #секунда остановки
        self.adult_mode = adult_mode    #ограничение по возрасту

class UrTube(User, Video):
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None
        self.video_titles = set()

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print("Пользователь не найден")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            lower_title = video.title.lower()           # преобразуем заголовок в нижний регистр
            if lower_title not in self.video_titles:    # проверяем наличие заголовка в множестве
                self.videos.append(video)               # добавляем видео в список
                self.video_titles.add(lower_title)      # добавляем заголовок в множество

    def get_videos(self, search_word):
        search_word = search_word.lower()               #преобразуем поисковое слово в нижний регистр
        watching_videos = list()
        for video in self.videos:
            if search_word in video.title.lower():      #ищем поисковое слово в списке заголовков в нижнем регистре
                watching_videos.append(video.title)
        return watching_videos

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = None
        for v in self.videos:               #поиск видео в списке
            if v.title == title:            #проверка совпадения заголовка видео
                video = v                   #присваиваем текущее значение поиска
                break

        if not video:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Начало воспроизведения видео: {video.title}")
        for second in range(video.time_now, video.duration + 1):
            print(second)
            time.sleep(1)
        print("Конец видео")
        video.time_now = 0

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')