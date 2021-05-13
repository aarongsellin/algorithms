def QuickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else: 
        pivot = sequence.pop()

    itemsGreater = []
    itemsLower = []

    for item in sequence:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)

    return quick_sort(itemsLower) + [pivot] + quick_sort(itemsGreater)

print(QuickSort([0,4,23,5,2,234,34,4,2,44,3]))