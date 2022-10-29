import numpy as np

arr = np.array([3, 5, 6, 7, 8, 9, 2, 0], dtype=float)


def add_rand(arr):
    for i in range(0, len(arr)):
        add = np.random.uniform(0, arr[i] * 0.08)
        arr[i] = arr[i] - add

np.savetxt("my_data.csv", arr, delimiter=",")