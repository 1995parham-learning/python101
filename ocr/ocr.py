from os import listdir
from os.path import isfile, join

# Replace with the output directory of TextRecognitionDataGenerator (trdg) on your machine.
print(listdir("/home/raha/py/src/TextRecognitionDataGenerator/trdg/out"))
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]