import math

arr, target = [3, 8, 15, 20, 25, 30, 35, 40, 45, 50], 25

def linear_search(arr, t): 
    return next((i for i, v in enumerate(arr) if v == t), -1)

def binary_search(arr, t):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == t: return m
        l, r = (m + 1, r) if arr[m] < t else (l, m - 1)
    return -1

def jump_search(arr, t):
    n, step, p = len(arr), int(math.sqrt(len(arr))), 0
    while p < n and arr[p] < t: p += step
    return next((i for i in range(p - step, min(p, n)) if arr[i] == t), -1)

print("linear search:", linear_search(arr, target), "\nbinary search:", binary_search(arr, target), "\njump search:", jump_search(arr, target))



