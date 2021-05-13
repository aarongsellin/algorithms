def InsertionSort(sequence):
    # We start at one since one value in a list is considerd sorted
    indexingLength = range(1, len(sequence))

    for i in indexingLength:
        valueToSort = sequence[i]

        while sequence[i-1] > valueToSort and i > 0: # Greater than zero is needed since Python allows negative indexing
            # Switch the values around
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            # Increment down
            i = i - 1

    return sequence

print(InsertionSort([2,4,5,56,62,3,4,56,32,4,6]))