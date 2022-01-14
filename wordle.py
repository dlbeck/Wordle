import sys
import json

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

def generatePossibleWords(engDict, outline, knownLetters, disallowedLetters):
	words = filter(lambda word: word.islower() and word.isalpha(), engDict)

	words = filter(lambda word: len(word) == len(outline), words)
	words = filter(lambda word: followsOutline(word, outline), words)
	words = filter(lambda word: containsChars(word, knownLetters), words)
	words = filter(lambda word: doesNotContainChars(word, disallowedLetters), words)
	return list(words)

# Assumes length of word in words is equal to length of outline
def guess(words, letterFreq, outline):
	highestScore = 0
	bestWord = ""
	for word in words:
		score = 0
		for i in range(len(outline)):
			if outline[i] == "_":
				score = score + letterFreq[word[i]]
		if score > highestScore:
			highestScore = score
			bestWord = word
	if highestScore == 0:
		return
	return bestWord


def main():
	outline = sys.argv[1]
	knownLetters = sys.argv[2]
	disallowedLetters = sys.argv[3]

	engDict = [word.strip().lower() for word in open("dictionary.txt")]
	letterFreq = json.load(open("letter_freq.json"))

	words = generatePossibleWords(engDict, outline, knownLetters, disallowedLetters)
	print(words)
	word = guess(words, letterFreq, outline)
	print(word)
	
if __name__ == "__main__":
    main()