import time
import concurrent.futures


def fibonacci(n):
    prev = 0
    num = 1
    for i in range(n):
        prev, num = num, num + prev
    return num


def count_time(func, arg):
    start = time.time()
    func(arg)
    return time.time() - start


def call_pure_fibonacci(arg):
    ans = list(map(fibonacci, arg))
    return ans


def call_thread_fibonacci(arg):
    ans = list(concurrent.futures.ThreadPoolExecutor(max_workers=10).map(fibonacci, arg))
    return ans


def call_process_fibonacci(arg):
    ans = list(concurrent.futures.ProcessPoolExecutor(max_workers=10).map(fibonacci, arg))
    return ans


if __name__ == '__main__':
    arg = [100, 2000, 30000, 400000, 500000, 100, 2000, 30000, 400000, 500000, ]
    file = open('artifacts/easy.txt', 'w')
    file.write(f'pure python: {count_time(call_pure_fibonacci, arg)}\n')
    file.write(f'Treads: {count_time(call_thread_fibonacci, arg)}\n')
    file.write(f'Processes: {count_time(call_process_fibonacci, arg)}\n')

