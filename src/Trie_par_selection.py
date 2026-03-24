def selection_sort(array):
    n = len(array)
    for i in range(0, n - 1):
        minpos = i
        for j in range(i + 1, n):
            if array[j] < array[minpos]:
                minpos = j
        array[i], array[minpos] = array[minpos], array[i]
    return array