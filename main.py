import time
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr



insertion_sort_times = []
merge_sort_times = []
n_values = np.geomspace(1, 10000, num=20, dtype=int) # like logspace but with defined ends

for n in n_values:
    
    arr = np.random.randint(low=1, high=max(2, n), size=n)
    
    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_sort_times.append(time.time() - start_time)

    start_time = time.time()
    merge_sort(arr.copy())
    merge_sort_times.append(time.time() - start_time)


plt.figure(figsize=(11, 8))
plt.plot(n_values, insertion_sort_times, label='Insertion Sort', marker='o')
plt.plot(n_values, merge_sort_times, label='Merge Sort', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Merge Sort vs. Insertion Sort')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()