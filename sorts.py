def bubble_sort(array):  # пузырьком
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def sift(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[i] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        sift(array, n, largest)


def heap_sort(array):  # пирамидальная

    n = len(array)
    for i in range(int(n / 2), -1, -1):
        sift(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        sift(array, i, 0)
    return array


def merge_sort(array):  # слиянием
    if len(array) >= 2:
        middle = int(len(array) / 2)
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1
        return array
    return array
