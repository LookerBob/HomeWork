from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname in [user.nickname for user in self.users]:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]

    def add(self, *args):
        for arg in args:
            if arg.title not in [video.title for video in self.videos]:
                self.videos.append(arg)

    def get_videos(self, search):
        output = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                output.append(video.title)
        return output

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        for video in self.videos:
            if video.title == title:
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(f'{video.time_now}', end=" ")
                    sleep(1)
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)
v4 = Video('test', 55)

# Добавление видео
ur.add(v1, v2, v3, v4, v3, v2, v1)

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
