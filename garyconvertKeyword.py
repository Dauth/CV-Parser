__author__ = 'Gary Wong'
import json
import sys

filename = "2.txt"
sampleFile = open(filename, 'r')
text = sampleFile.read()
myList = []
myList.append(text)
with open('2.json', 'w') as outfile:
    json.dump(myList, outfile)
