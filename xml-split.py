import fileinput

content = ""
dataPath = ""

def containDataPath(line):
    line = line.strip()
    if ("android:pathData" in line):
        return True
    return False

def extractDataPath(line):
    return line.split("\"", 1)[1].split("\"", 1)[0]

def main():
    for line in fileinput.input():
        if (containDataPath(line)):
            dataPath = extractDataPath(line)
            print(dataPath)

main()

outputFile = open('output', 'w')
outputFile.write(content)
outputFile.close()
