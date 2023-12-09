import sys

if (len(sys.argv) != 2):
    raise Exception(f"Expected 1 argument got {len(sys.argv)-1}!")


def wordToNumber(input: str) -> str:
    buffer = ""
    for i in input:
        buffer += i
        buffer = (buffer
            .replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e"))
    return buffer


total = 0
with open(sys.argv[1]) as puzzleInput:
    for Line in puzzleInput.readlines():
        Line = wordToNumber(Line)
        firstNum = ""
        lastNum = ""
        for character in Line:
            if character.isnumeric():
                if firstNum == "":
                    firstNum = character
                lastNum = character
        total += int(firstNum + lastNum)
print(total)
