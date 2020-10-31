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

def main():
    pathData = ""
    upperTemplate = ""
    lowerTemplate = ""
    foundPathData = False
    for line in fileinput.input():
        if (containPathData(line)):
            foundPathData = True
            pathData = extractPathData(line)
            upperTemplate += getFirstHalf(line)
            lowerTemplate += getSecondHalf(line)
        else:
            if foundPathData:
                lowerTemplate += line
            else:
                upperTemplate += line

    outputFile = open('output', 'w')
    outputFile.write(upperTemplate)
    outputFile.write(lowerTemplate)
    outputFile.close()

main()

