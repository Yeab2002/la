def find_maximum(arr):
    if not arr:
        return None
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

# Test find_maximum function
print("Maximum element in the array:")
print(find_maximum([1, 2, 3, 4, 5]))  # Output: 5
