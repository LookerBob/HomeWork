import threading
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        i = 1
        while i <= word_count:
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
            i += 1
    print(f'Завершилась запись в файл {file_name}')


started_at = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = datetime.now()
print(f'Работа потоков {ended_at - started_at}')
thr = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]
started_at = datetime.now()
threads = [threading.Thread(target=write_words, args=args) for args in thr]
for t in threads:
    t.start()

for t in threads:
    t.join()
ended_at = datetime.now()
print(f'Работа потоков {ended_at - started_at}')
