num1 = None
num2 = None

with open('UniqueOutput.txt', 'r') as readFile:
    with open('SampleMissingNumbers.txt', 'a') as writeFile:
        num1 = int(readFile.readline())
        num2 = int(readFile.readline())
        while True:
            num1, num2 = num2, readFile.readline()
            if str(num2) == '':
                break
            num2 = int(num2)
            if ((num2 - num1) == 1):
                continue
            while (num2 - num1 > 1):
                num1 += 1
                writeFile.write(str(num1))
                writeFile.write('\n')