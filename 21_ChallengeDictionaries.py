#List out all the words in a given sentence for each vowel .
#Erroring out.Have to check back

wordsentence=input('Enter the sentence:')
words=wordsentence.split()
wordvowelslist=['a','e','i','o','u']
worddictionary={}
dictlist=[]
value=''

for word in words:
    #print (word)
    for letter in word:
        #print (letter)ssa
        if letter in wordvowelslist:
            dictlist=[]
            value=''
            if worddictionary.get(letter) == None:
                #if key doesn't exist add it 
                worddictionary[letter] = word
            else:
                #print (worddictionary)
                value=worddictionary[letter]
                dictlist.append(value)
                if value!=word:
                    dictlist.append(word)
                    worddictionary[letter]=dictlist
    print (worddictionary)


#Count the number of times a word occurred in a sentence and list in desc order
#satish lives in bethpage bethpage is where satish lives in bethpage
countsentence=input('Enter the sentence:')
sentlist=countsentence.split()
countdict={}
countlist=[]

for word in sentlist:
    if countdict.get(word)==None:
        countdict[word] = 1
    else:
        countdict[word]=countdict[word]+1

print (countdict)

for word in countdict:
    countlist.append([word,countdict[word]])

print (countlist)


def sortcriteria(ls):
    return ls[1]
countlist.sort(key=sortcriteria,reverse=True)#reverse=true helps to give the o/p in decreasing order
print (countlist)