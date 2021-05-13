# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def FirstUniqueCharacter(sentence):
    # Create a dict to store the frequency of which chars appear
    frequency = {}

    # Convert sentence to lower case
    sentence = sentence.lower()

    for char in sentence:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    for i in frequency:
        if frequency[i] == 1:
            return i

    # There are no unique characters
    return -1

print(FirstUniqueCharacter("Hey, how are you doing?"))