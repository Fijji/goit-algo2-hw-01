import random

def quick_select(arr, left, k):
    if len(arr) == 1:
        return arr[0]

    selected = random.choice(arr)
    left_part = [x for x in arr if x < selected]
    mid_part = [x for x in arr if x == selected]
    right_part = [x for x in arr if x > selected]

    if k <= len(left_part):
        return quick_select(left_part, left, k)
    elif k <= len(left_part) + len(mid_part):
        return selected
    else:
        return quick_select(right_part, left, k - len(left_part) - len(mid_part))

arr = [7, 10, 4, 3, 20, 15, 99, 16]
k = 3
result = quick_select(arr, 0, k)
print(f"{k}-smallest element in unsorted array is: {result}")
