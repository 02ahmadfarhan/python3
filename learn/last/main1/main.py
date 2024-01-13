#!/usr/bin/python3
words = []

def readFile():
    global words
    with open("wordfile.txt", "r") as wordFile:
        words = wordFile.readlines()
        wordFile.close

def sortTheArray(words):
    words.sort()
    print(words)

def writeFile(sorted_words):
    with open("wordfile-sorted.txt", "w") as wordFile:
        wordFile.writelines(sorted_words)

def main():
    words = readFile()  # Read the file and get the list of words
    sorted_words = sortTheArray(words)  # Sort the list of words
    writeFile(sorted_words)  # Write the sorted list to a new file

if __name__ == "__main__":
    main()
