def checkEqualFrequency(inputArray):
    return True if len(set([ inputArray.count(x) for x in inputArray])) == 1 else False
print(checkEqualFrequency([1, 2, 2, 3, 1, 3, 1, 3]))