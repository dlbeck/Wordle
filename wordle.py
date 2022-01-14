import sys

# outline contains "_" for wildcard characters. Ex) "am_e_"
def followsOutline(word, outline):
	if len(word) != len(outline):
		return False
	for i in range(len(word)):
		if outline[i] == "_":
			continue
		elif word[i] != outline[i]:
			return False
	return True

def containsChars(word, chars):
	for c in chars:
		if not c in word:
			return False
	return True

def doesNotContainChars(word, chars):
	for c in chars:
		if c in word:
			return False
	return True


def main():
	outline = sys.argv[1]
	knownLetters = sys.argv[2]
	disallowedLetters = sys.argv[3]

	words = [word.strip().lower() for word in open("dictionary.txt")]
	
	words = filter(lambda word: word.islower() and word.isalpha(), words)
	words = filter(lambda word: len(word) == 5, words)
	words = filter(lambda word: followsOutline(word, outline), words)
	words = filter(lambda word: containsChars(word, knownLetters), words)
	words = filter(lambda word: doesNotContainChars(word, disallowedLetters), words)

	for word in words:
		print(word)
	

if __name__ == "__main__":
    main()