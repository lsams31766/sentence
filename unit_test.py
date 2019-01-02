#unit_test.py

#test sentence class

from longest import sentence

nbrTests = 0
nbrPassed = 0
nbrFailed = 0

def RunTest(testSentence, correctLength, correctWord):
	global nbrTests, nbrPassed, nbrFailed
	nbrTests += 1
	objSentence = sentence(testSentence)
	resultLength, resultWord = objSentence.getLongest()
	if (resultLength == correctLength) and (resultWord == correctWord):
		nbrPassed += 1
	else:
		nbrFailed += 1
		print 'FAILED test %d given: %s,%d,%s' % (nbrTests, testSentence, correctLength, correctWord)

#Run Unit Tests on class sentence
#format for arguments: testSentence, correctLength, correctWord
RunTest('The Cow Jumped Over the Moon',6,'Jumped') # all alphas and spaces
RunTest('The ##@Cow !!!!!s !$ver the Moon,,',4,'Moon') # any character
RunTest('T h e c o w j u',1,'T') #return first char if all the same
print 'Results: Passed %d Failed %d out of %d Tests' % (nbrPassed,nbrFailed,nbrTests)
# make it fail for wrong word, worng length
print 'The next 2 tests will FAIL on purpose:'
RunTest('The Cow Jumped Over the Moon',9,'Jumped') #
RunTest('The Cow Jumped Over the Moon',6,'Over') #
print 'Make Fail - Results: Passed %d Failed %d out of %d Tests' % (nbrPassed,nbrFailed,nbrTests)
