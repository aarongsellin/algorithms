def LinearSearch(lst, key):
    if len(lst) <= 0: # Sanity check
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i  # If found return index
    return -1 # Return 1 otherwise

# Driver code
if __name__ == "__main__":
    lst = [5, 4, 3, 2, 1]
    key = 4

    index = LinearSearch(lst, key)
    if index != -1:
        print("Key: {} is found at index: {}".format(key,index))
    else:
        print("Key: {} was not found in the list".format(key))