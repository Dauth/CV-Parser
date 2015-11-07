__author__ = 'Owner'
import jsonpickle, json

def encodeClassToJson(inputClass):
    return jsonpickle.encode(inputClass)

def decodeJsonToClass(inputJson):
    return jsonpickle.decode(inputJson)

def saveFile(fileLocation, tempList, keyword):
    fileName = ''.join((fileLocation, keyword, '.json'))
    with open(fileName, 'w') as outfile:
        json.dump(tempList, outfile, indent=1, ensure_ascii=False)
    print('saved')

def openFile(eFile):
    with open(eFile, encoding='utf-8') as inFile:
        return json.load(inFile)


