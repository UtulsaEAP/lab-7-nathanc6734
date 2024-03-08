'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''

def wordInRange():
    #Type your code here
    filename = input()
    start = input()
    end = input()
    file = open(filename)
    lines = (file.readlines())
    for x in range(len(lines)):
        if start <= lines[x].rstrip() <= end:
            print(f"{lines[x].rstrip()} - in range")
        else:
            print(f"{lines[x].rstrip()} - not in range")
    return
if __name__ == '__main__':
    wordInRange()