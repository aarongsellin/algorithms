# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

def AverageWordLength(sentence):
    for p in "!?',;.":
        # Replace all stops
        sentence = sentence.replace(p, '')

    # Split the sentence into individual words
    words = sentence.split()

    # Return the average
    return round(sum(len(word) for word in words)/len(words),2)

print(AverageWordLength("Hey how are you doing? It's is a fine day today..."))