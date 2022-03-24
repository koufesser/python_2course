import math
import time
import concurrent.futures as con


def integrate(f, a, b, exec, n_iter=10 ** 8):
    step = (b - a) / n_iter
    arr = []
    for i in range(n_iter):
        arr.append(a + i * step)
    return sum(list(exec.map(f, arr)))


def count_time(func, *arg):
    start = time.time()
    func(*arg)
    return time.time() - start


if __name__ == '__main__':
    f = open('artifacts/medium.txt', 'w')
    for i in range(1, 16):
        f.write(f'Threads with {i} max_workers and iter == 1000 : {count_time(integrate, math.sin , 0, math.pi, con.ThreadPoolExecutor(max_workers=i))}\n')
    f.write('\n')
    for i in range(1, 16):
        f.write(f'Processes with {i} max_workers and iter == 1000 : {count_time(integrate, math.sin , 0, math.pi, con.ProcessPoolExecutor(max_workers=i))}\n')
