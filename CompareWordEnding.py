def solution(string, ending):
    endingLength = len(ending)
    print(str(endingLength) + ": ending length")
    stringLength = len(string)
    print(str(stringLength)+ ": string length" )
    lengthDiffrence = stringLength - endingLength
    print(str(lengthDiffrence) + ": length diffrence")
    int(lengthDiffrence)
    int(stringLength)
    wordEnding = string[lengthDiffrence, stringLength]
    print(str(wordEnding) +" : Word ending" )


solution("abcd", "cd")