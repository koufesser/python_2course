import time
import threading
import multiprocessing

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
    for i in range(15):
        fibonacci(arg)


def call_thread_fibonacci(arg):
    ar = []
    for i in range(15):
        t = threading.Thread(target=fibonacci, args=(arg,))
        t.start()
        ar.append(t)
    for i in ar:
        i.join()


def call_process_fibonacci(arg):
    ar = []
    for i in range(15):
        m = multiprocessing.Process(target=fibonacci, args=(arg, ))
        m.start()
        ar.append(m)
    for i in ar:
        i.join()


if __name__ == '__main__':
    arg = 100000
    file = open('artifacts/easy.txt', 'w')
    file.write(f'pure python: {count_time(call_pure_fibonacci, arg)}\n')
    file.write(f'Treads: {count_time(call_thread_fibonacci, arg)}\n')
    file.write(f'Processes: {count_time(call_process_fibonacci, arg)}\n')

