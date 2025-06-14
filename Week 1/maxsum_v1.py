import time
start = time.process_time()

def Sum(x, i, j):
    s = 0
    for k in range(i, j + 1):
        s += x[k]
    return s

def max_contiguous_sum(arr):
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            current_sum = Sum(arr, i, j)
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

arr = list(map(int, input().split()))
print("Maximum contiguous sum:", max_contiguous_sum(arr))

finish = time.process_time()
print("Running time =", finish - start, "seconds")
