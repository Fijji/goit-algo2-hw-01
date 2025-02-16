def find_min_max(arr, left, right):
    if left == right:
        return arr[left], arr[left]

    mid = (left + right) // 2
    min1, max1 = find_min_max(arr, left, mid)
    min2, max2 = find_min_max(arr, mid + 1, right)

    return min(min1, min2), max(max1, max2)

arr = [1, -8, 1, 9, -6, 7, -3, 13]
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)

print(f"Min value: {min_val}")
print(f"Max value: {max_val}")

