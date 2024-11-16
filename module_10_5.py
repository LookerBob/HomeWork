import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as file:
        data = file.readline()
        while data:
            all_data.append(data[:-1])
            data = file.readline()


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # Линейный вызов
    start = datetime.now()
    for files in filenames:
        read_info(files)
    end = datetime.now()
    print(f'{end - start} (линейный)')
    # Многопроцессный
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start} (многопроцессный)')
