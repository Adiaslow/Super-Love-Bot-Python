import re
from random import randint
from datetime import date, datetime

with open("scraped-love.txt","r") as scrapings:
    text = scrapings.read()

cleanText = re.sub(r'[^\w]', ' ', text)

lowerCaseText = cleanText.lower()

wordCount = len(cleanText.split()) 

wordList = lowerCaseText.split()

# print(wordCount)

# print(cleanText)

desiredNumOfWords = randint(5, 13)

print(desiredNumOfWords)

sentence = ''

for i in range(0, desiredNumOfWords, 1):
    if i != desiredNumOfWords - 1:
        sentence += wordList[randint(0, wordCount)] + " "
    else:
        sentence += wordList[randint(0, wordCount)]

sentence += "."
sentence = sentence[0].upper() + sentence[1:]

print(sentence)

now = str(datetime.now())
fileName = re.sub(r'[^\w]', ' ', now)
fileSuffix = str(".txt")
fileName = now + fileSuffix



print(fileName)

sentenceFile = open(fileName, "w")