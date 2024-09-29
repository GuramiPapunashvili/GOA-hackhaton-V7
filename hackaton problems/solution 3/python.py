def remove_mid(arr):
    if len(arr) % 2 == 0:
        raise ValueError("The list has an even number of elements.")

    return arr[:len(arr) // 2] + arr[len(arr) // 2 + 1:]

result = remove_mid([5, 36, 3, 4, 6, 3, 5, 2, 2])
print(result)