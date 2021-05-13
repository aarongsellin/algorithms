# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def ValidPalindrome(sentence):
	sentence = sentence.lower()

	for i in range(len(sentence)):
		t = sentence[:i] + sentence[i+1:]
		if t == t[::-1]: 
			return True
	return sentence == sentence[::-1]

print(ValidPalindrome("tenet"))