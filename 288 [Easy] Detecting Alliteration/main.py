# [2016-10-17] Challenge #288 [Easy] Detecting Alliteration
# https://www.reddit.com/r/dailyprogrammer/comments/57zcbm/20161017_challenge_288_easy_detecting_alliteration/

stopWords = ['I', 'a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'com', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'this', 'to', 'was', 'what', 'when', 'where', 'who', 'will', 'with', 'the']
inputArray = ['3', 'Peter Piper Picked a Peck of Pickled Peppers', 'Bugs Bunny likes to dance the slow and simple shuffle', 'You\'ll never put a better bit of butter on your knife']

def main():
    num_sentences = int(inputArray[0])

    for i in range(1, num_sentences + 1):
    	sentence = [word for word in inputArray[i].split() if word not in stopWords]
    	pastWord = " "
    	inAlit = False
    	alit = []
    	for index, word in enumerate(sentence):
    		foundAlit = False
    		if word[0].lower() == pastWord[0].lower():
    			foundAlit = True
    			if not inAlit:
    				alit.append(sentence[index-1])
    				alit.append(word)
    			else:
    				alit.append(word)
    		inAlit = foundAlit
    		pastWord = word
    	print(" ".join(alit))

if __name__ == "__main__":
    main()