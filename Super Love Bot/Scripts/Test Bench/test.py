msg = "Mess your breathe as any was teach who for not for to I."
print(msg)

print("*****")

numLines = 6
charPerLine = 10
wordCount = 13
totalChars = numLines * charPerLine

words = msg.split()

print(words)
    
print("*****")

letPerWord = {w:len(w) for w in words}

for key in letPerWord:
    print(key, ">", letPerWord[key])
    
print(letPerWord)
    
print("*****")

"""
for i in range(0, len.words, 1):
    
    if len.words[i] + len.words[i + 1] +  <:

    else:
"""


newMsg = words[0] + "-"

for i in range(1, wordCount, 1):
    if i + 1 < wordCount:
        if len(words[i]) + 1 + len(words[i + 1]) + 1 < 10:
            newMsg += words[i] + "-"
        
        else:
            newMsg += words[i] + "-\n"
""" 
    if i + 2 < wordCount:
        if len(words[i]) + 1 + len(words[i + 1]) + 1 + len(words[i + 2]) < 10:
            newMsg += words[i] + "-"
        
        else:
            newMsg += words[i] + "-\n"
"""

newMsg += words[wordCount - 1]
    
print(newMsg)