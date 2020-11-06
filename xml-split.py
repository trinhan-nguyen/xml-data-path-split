import fileinput

def containPathData(line):
    line = line.strip()
    if ("android:pathData" in line):
        return True
    return False

def extractPathData(line):
    return line.split("\"", 1)[1].split("\"", 1)[0]

def getFirstHalf(line):
    return line.split("\"", 1)[0]

def getSecondHalf(line):
    return line.split("\"", 1)[1].split("\"", 1)[1]

def splitPathData(pathData):
    return pathData.split("M")

def writeToFile(content):
    outputFile = open('output', 'w')
    for item in content:
        outputFile.write(item)
    outputFile.close()

def main():
    pathData = ""
    upperTemplate = ""
    lowerTemplate = ""
    foundPathData = False
    paths = []
    for line in fileinput.input():
        if (containPathData(line)):
            foundPathData = True
            pathData = extractPathData(line)
            upperTemplate += getFirstHalf(line)
            lowerTemplate += getSecondHalf(line)
            paths = splitPathData(pathData)
        else:
            if foundPathData:
                lowerTemplate += line
            else:
                upperTemplate += line
    writeToFile(paths)


main()

