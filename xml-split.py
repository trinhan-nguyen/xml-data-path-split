import fileinput

DELIMITER = "M"

def containPathData(line):
    line = line.strip()
    if ("android:pathData" in line):
        return True
    return False

def extractPathData(line):
    return line.split("\"", 1)[1].split("\"", 1)[0]

def getFirstHalf(line):
    return line.split("\"", 1)[0] + "\""

def getSecondHalf(line):
    return "\"" + line.split("\"", 1)[1].split("\"", 1)[1]

def splitPathData(pathData):
    paths = pathData.split(DELIMITER)
    for i in range(1, len(paths)):
        if paths[i]:
            paths[i] = DELIMITER + paths[i]
    return paths

def postProcess(paths, lower, upper):
    for i in range(len(paths)):
        paths[i] = upper + paths[i] + lower
    return paths

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

    content = postProcess(paths, lowerTemplate, upperTemplate)
    writeToFile(content)

main()

