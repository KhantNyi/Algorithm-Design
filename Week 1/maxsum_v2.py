
import time
start = time.process_time()

def prefix_sum(arr):
    acc = [0] * len(arr)
    acc[0] = arr[0]
    for i in range(1, len(arr)):
        acc[i] = acc[i - 1] + arr[i]
    return acc

def Sum(acc, i, j):
    if i == 0:
        return acc[j]
    else:
        return acc[j] - acc[i - 1]

def max_subarray_sum_brute_force(arr):
    acc = prefix_sum(arr)
    n = len(arr)
    max_sum = arr[0]

    for i in range(n):
        for j in range(i, n):
            current_sum = Sum(acc, i, j)
            max_sum = max(max_sum, current_sum)

    return max_sum

arr = list(map(int, input().split()))

max_sum = max_subarray_sum_brute_force(arr)
end = time.process_time()

# Output
print("Maximum contiguous sum (O(n²)):", max_sum)
print("Time taken:", end - start, "seconds")
