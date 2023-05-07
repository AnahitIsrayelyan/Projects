num1 = None
num2 = None

with open('sampleOutput.txt', 'r') as readFile:
    with open('UniqueOutput.txt', 'a') as writeFile:
        num1 = readFile.readline()
        num2 = readFile.readline()
        while True:
            if num2 == '':
                writeFile.write(num1)
                break
            if num1 == num2:
                num1, num2 = num2, readFile.readline()
                continue
            else:
                writeFile.write(num1)
                num1, num2 = num2, readFile.readline()