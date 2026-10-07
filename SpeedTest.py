import time
import sys
import requests


def SpeedTests(url, headers):
    print('Начался процес замера скорости...')
    times = []
    Mbit = []
    for i in range(10):
        start_time = time.perf_counter()
        response = requests.get(url, headers=headers)
        end_time = time.perf_counter()
        speed_time = end_time - start_time
        MB = len(response.content) / 1048576
        times.append(speed_time)
        Mbit.append(MB)

    average_time = sum(times) / len(times)
    sum_MB = sum(Mbit)
    speed = sum_MB / sum(times)
    print('Процесс замера скорости завершен результаты:')
    return (f'Среднее время скачивания 1 файла: {average_time:.2f} сек. \n'
            f'Обьем скаченных файлов: {sum_MB:.2f} Mb \n'
            f'Скорость скачивания: {speed:.2f} Mb/s')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input('ВВедите URL ссылки для проверки:')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Cache-Control': 'no-cache'
    }

    result = SpeedTests(url, headers)
    print(result)