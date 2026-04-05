def selection_sort(array, key):
    n = len(array)
    for i in range(n - 1):
        minpos = i
        for j in range(i + 1, n):
            if array[j][key] < array[minpos][key]:
                minpos = j
        array[i], array[minpos] = array[minpos], array[i]
    return array
