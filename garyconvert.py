__author__ = 'Gary Wong'
import json
import sys

print (sys.argv[1])
filename = "data/" + sys.argv[1] + ".txt"
sampleFile = open(filename, 'r')
text = sampleFile.read()
myList = []
myList.append(text)
with open('1.json', 'w') as outfile:
    json.dump(myList, outfile)
