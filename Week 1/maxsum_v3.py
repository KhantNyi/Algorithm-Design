import time
start = time.process_time()

def kadane(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Read input from file redirection
arr = list(map(int, input().split()))
print("Maximum contiguous sum (Kadane's):", kadane(arr))

finish = time.process_time()
print("Running time =", finish - start, "seconds")

