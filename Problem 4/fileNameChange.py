"""
Name: Nathan Carr
Lab Time: Thursday @ 2pm
"""

def fileNameChange():
    #type your code here
    filename = input()
    filelines = open(filename).readlines()
    newlines = []
    for x in range(len(filelines)):
        text = filelines[x].replace("photo.jpg", "info.txt")
        newlines.append(text)
    print(newlines)
    return

if __name__ == '__main__':
    fileNameChange()