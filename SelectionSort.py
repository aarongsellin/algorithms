def SelectionSort(sequence):
    indexingLength = range(0, len(sequence) - 1)

    for i in indexingLength:
        minValue = i

        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[minValue]:
                minValue = j

        if minValue != i:
            # Switch the values around
            sequence[minValue], sequence[i] = sequence[i], sequence[minValue]

    return sequence

print(SelectionSort([4,3,5,76,2,23,45]))