num = 1

nums_in_each_file = 50
eof = False
with open('sample.txt', 'r') as readFile:
    while not eof:
        filename = 'sample' + str(num)
        num += 1
        print(filename)
        with open(filename, 'a') as writeFile:
            list_to_sort = []
            for _ in range(nums_in_each_file):
                read_num = readFile.readline()
                if read_num == '':
                    eof = True
                    break
                list_to_sort.append(int(read_num))
            list_to_sort.sort()
            for i in list_to_sort:
                writeFile.write(str(i))
                writeFile.write('\n')
    print("DONE")