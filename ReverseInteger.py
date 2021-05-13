# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def ReverseInteger(x):
    string = str(x)

    if string[0] == "-":
        # Negative value, return a reversed list
        return int("-" + string[:0:-1])
    else:
        # Return a reversed list
        return int(string[::-1])

print(ReverseInteger(123))