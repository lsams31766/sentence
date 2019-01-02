#longest.py

class sentence():
	def __init__(self, theSentence):
		self.theSentence = theSentence

	def getLongest(self):
		#remove non alphabetic characters, but not spaces
		legal = 'abcdefghihjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
		text = ''.join([c for c in self.theSentence if c in (legal)])
		#put each word into a split by splitting at space
		l = text.split(' ')
		longestLength = 0
		longestWord = ''
		#get longest length and word
		for word in l:
			if len(word) > longestLength:
				longestLength = len(word)
				longestWord = word
		return longestLength,longestWord

def main():
	testSentence = 'The cow jumped over the moon.'
	objSentence = sentence(testSentence)
	longestWord,longestLength = objSentence.getLongest()
	print 'longest length: %d, longest word: %s' % (longestWord,longestLength)

if __name__ == '__main__':
	main()

