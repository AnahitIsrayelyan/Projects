# here we will generate random numbers' chunks, save them in a list, then write in a file

from random import randint

max_value = 2**32 - 1
# as soon as numbers in python are objects and aren't 4 bytes, numbers_to_generate != 4 bln
numbers_to_generate = 250000000
numbers_each_loop = 500000

# i = randint(0, max_value)
# import sys
# print(sys.getsizeof(i))
# print(sys.getsizeof(str(i)))

num = 1

while numbers_to_generate > 0:
    nums_list = []
    for _ in range(min(numbers_each_loop, numbers_to_generate)):
        nums_list.append(randint(0, max_value))

    with open('myfile.txt', 'a') as my_file:
        for i in nums_list:
            my_file.write(str(i))
            my_file.write('\n')
    numbers_to_generate -= min(numbers_to_generate, numbers_each_loop)
    print(num,"/500")
    num += 1
 
