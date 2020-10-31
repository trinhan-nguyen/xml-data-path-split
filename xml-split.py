import fileinput

def containDataPath(line):
    line = line.strip()
    if ("android:pathData" in line):
        return True
    return False

def extractDataPath(line):
    return line.split("\"", 1)[1].split("\"", 1)[0]

def getFirstHalf(line):
    return line.split("\"", 1)[0]

def getSecondHalf(line):
    return line.split("\"", 1)[1].split("\"", 1)[1]

def main():
    dataPath = ""
    upperTemplate = ""
    lowerTemplate = ""
    foundDataPath = False
    for line in fileinput.input():
        if (containDataPath(line)):
            foundDataPath = True
            dataPath = extractDataPath(line)
            upperTemplate += getFirstHalf(line)
            lowerTemplate += getSecondHalf(line)
        else:
            if foundDataPath:
                lowerTemplate += line
            else:
                upperTemplate += line

    outputFile = open('output', 'w')
    outputFile.write(upperTemplate)
    outputFile.write(lowerTemplate)
    outputFile.close()

main()

