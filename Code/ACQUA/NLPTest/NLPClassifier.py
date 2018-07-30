import os
import random
from Classification import classify

allWords = []

# loads in the provided word sets in the directory "/data/wordLists"
def setup():
    path = "data/wordLists"
    for filename in os.listdir(os.getcwd()+"/"+path):
        # so .DS_Store isn't loaded in
        if  filename[0] != "." :
            with open(path +"/"+filename, errors='ignore') as file:
                print("loaded in " + filename)
                newWords = []
                for line in file:
                    newWords.append(line)
                allWords.append(newWords)



# file must be a CSV with the classification as the 1st element and the tweet/ text as the 2nd
def classifyText(filename):

    # Dictionary of classification to array of tweets
    textDict = {}

    numText = 0
    # Load in the files
    with open(filename) as file:
        for line in file :
            numText +=1

            parts = line.split(",")

            parts[1]= parts[1][1:-2]


            if textDict.get(parts[0]) is None:
                textDict[parts[0]] = [parts[1]]
            else :
                textDict.get(parts[0]).append(parts[1])


    with open("data/temp.csv", "w") as file:
        file.write(str(numText) + "," + "2,happy_words,sad_words\n")



    for k,v in textDict.items():
        writeToFile(k, v)

    classify(location="", file="temp.csv", class_labels=[r'H', r'S'])



# returns a number of how many times words in the text occurred in the given list
def correlateWords(text, words):
    # NB cannot return the same value for all tweets as this breaks the algorithm
    score = 1
    for word in text:
        if word in words :
            score += 1
    #return score
    return random.randint(1, 10)


def counts(text):
    global allWords
    outp = ""
    for words in allWords:
        res = correlateWords(text, words)
        outp += str(res) + ","

    return outp

def writeToFile(classification, arr):
    with open("data/temp.csv", "a") as file:
        for tweet in arr :
            file.write(counts(tweet) + str(classification) + "\n")



setup()
classifyText("data/tweets.txt")

