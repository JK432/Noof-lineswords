# Write a Python program to count the number of lines, words and characters in the input files.


with open("file.txt", 'r') as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print('\n Line number ::', len(line), '\n Words number ::', len(words), '\n Charecters ::', (len(data)-len(spaces)))