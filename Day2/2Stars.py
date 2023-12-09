import sys
from itertools import islice

if (len(sys.argv) != 2):
    raise Exception(f"Expected 1 argument got {len(sys.argv)-1}!")

validTotal = 0

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def parseLine(Line):
    finalList = []
    listFromLine = Line.partition(":")[2].strip().replace(",", "", -1).split(";")
    tempList=[]
    for i in listFromLine:
        tempList.append(split_list(i.strip().split(), 2))
    finalList.append(tempList)
    finalList.append(int(Line[5:].partition(":")[0]))
    return finalList

with open(sys.argv[1]) as puzzleInput:
    power = 0
    for Line in puzzleInput.readlines():
        isInvalid = False
        lineList = parseLine(Line)
        lineRmax = 0
        lineGmax = 0
        lineBmax = 0
        print(lineList)
        for i in lineList:
            if isinstance(i, int):
                if (not isInvalid):
                    validTotal+=i
                    print(f"Game {i}: valid")
                else:
                    print(f"Game {i}: invalid")
            else:
                print("d")
                for k in i:
                    red = 0
                    green = 0
                    blue = 0
                    for j in k:
                        match j[1]:
                            case 'red':
                                red+=int(j[0])
                                if red>12:
                                    isInvalid=True
                            case 'green':
                                green+=int(j[0])
                                if green>13:
                                    isInvalid=True
                            case 'blue':
                                blue+=int(j[0])
                                if blue>14:
                                    isInvalid=True
                            case _:
                                print("_")
                    if red > lineRmax:
                        lineRmax = red
                    if green > lineGmax:
                        lineGmax = green
                    if blue > lineBmax:
                        lineBmax = blue
        power += lineRmax*lineGmax*lineBmax
print(f"total: {validTotal}")
print(f"power: {power}")