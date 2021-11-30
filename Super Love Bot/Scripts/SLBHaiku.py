import re

def haikuGen1():
    dataFile = '/Users/Adam/Desktop/Super Love Bot/Scrapings/goodreads-50-love-quotes.txt'
    
    with open(dataFile,"r") as scrapings:
        text = scrapings.read()

    cleanText = re.sub(r'[^\w]', ' ', text)
    
    lowerCaseText = cleanText.lower()
    
    wordList = lowerCaseText.split()
    
    # print(wordList)
    
    oneLetterList = []
    twoLetterList = []
    threeLetterList = []
    fourLetterList = []
    fiveLetterList = []
    sixLetterList = []
    sevenLetterList = []
    
    for i in range(0, len(wordList), 1):
        if len(lowerCaseText[i]) == 1:
            oneLetterList += wordList[i]
        if len(wordList[i]) == 2:
            twoLetterList += wordList[i]
        if len(wordList[i]) == 3:
            threeLetterList += wordList[i]
        if len(wordList[i]) == 4:
            fourLetterList += wordList[i]
        if len(wordList[i]) == 5:
            fiveLetterList += wordList[i]
        if len(wordList[i]) == 6:
            sixLetterList += wordList[i]
        if len(wordList[i]) == 7:
            sevenLetterList += wordList[i]
    
    # print(wordList)
    print(sevenLetterList)
            
haikuGen1()