import sys

if (len(sys.argv) != 2):
    raise Exception(f"Expected 1 argument got {len(sys.argv)-1}!")

total = 0
with open(sys.argv[1]) as puzzleInput:
    for Line in puzzleInput.readlines():
        firstNum = ""
        lastNum = ""
        for character in Line:
            if character.isnumeric():
                if firstNum == "":
                    firstNum = character
                lastNum = character
        total += int(firstNum + lastNum)
print(total)
