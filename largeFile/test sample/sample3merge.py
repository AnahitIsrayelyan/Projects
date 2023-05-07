files = []
num_of_files = 5
for i in range(1, num_of_files + 1):
    filename = 'sample' + str(i)
    files.append(open(filename, 'r'))


nums_to_sort = []      # here are integers
for i in files:
    numm = i.readline()
    if numm == '':
        i.close()
        files.remove(i)
    else:
        nums_to_sort.append(int(numm))

print(nums_to_sort)

num = 1
with open('sampleOutput.txt', 'a') as outputFile:
    while True:
        min_value = min(nums_to_sort)
        outputFile.write(str(min_value))
        outputFile.write('\n')
        min_val_index = nums_to_sort.index(min_value)
        tmp_val = files[min_val_index].readline()
        if tmp_val == '':
            files[min_val_index].close()
            del files[min_val_index]
            del nums_to_sort[min_val_index]
        else:
            nums_to_sort[min_val_index] = int(tmp_val)
        
        if nums_to_sort == []:
            break

        print('loop', num)
        num += 1
            
        
        