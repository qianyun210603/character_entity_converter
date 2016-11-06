#coding:utf-8

import os.path
import codecs
from chardet.universaldetector import UniversalDetector
import html

def convert_character_entity(inputFilename, outputFilename):
    if os.path.exists(outputFilename):
        os.remove(outputFilename)
    detector = UniversalDetector()
    with open(inputFilename, 'rb') as fileToDetect:
        for line in fileToDetect:
            detector.feed(line)
            if detector.done:
                break
            detector.close()
    mode = detector.result['encoding']
    with codecs.open(outputFilename, "x", "utf-8") as outFile, codecs.open(inputFilename, 'r', mode) as inFile:
        for line in inFile:
            converted_line = html.unescape(line)
            outFile.write(converted_line)

inputFilename = r'F:\Downloads\十国千娇_gb2312.txt'
outputFilename = inputFilename[:-4] + '_converted' + inputFilename[-4:]

convert_character_entity(inputFilename, outputFilename)

print(outputFilename)
