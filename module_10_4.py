from time import sleep
from queue import Queue
from threading import Thread
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            flag = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    table.guest.start()
                    flag = True
                    break
            if flag:
                continue
            self.queue.put(guest)
            print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        not_empty_table_and_empty_queue = True
        while not_empty_table_and_empty_queue:
            flag = False
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                if table.guest is not None:
                    flag = True
            if self.queue.empty():
                not_empty_table_and_empty_queue = flag


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = \
    [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
