from array import *


def fibonacci(n):
    arr = array('i', [])
    arr.append(1)
    arr.append(2)
    for j in range(2, n):
        arr.append(arr[j - 1] + arr[j - 2])
    return arr
