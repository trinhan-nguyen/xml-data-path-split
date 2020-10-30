import fileinput

content = ""

def containDataPath(line):
    line = line.strip()
    if ("android:pathData" in line):
        return True
    return False

def main():
    for line in fileinput.input():
        if (containDataPath(line)):
           print("yes") 

main()

outputFile = open('output', 'w')
outputFile.write(content)
outputFile.close()
