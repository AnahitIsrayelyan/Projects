from random import randint

max_value = 100
numbers_to_generate = 250
numbers_each_loop = 50

num = 1

while numbers_to_generate > 0:
    nums_list = []
    for _ in range(min(numbers_each_loop, numbers_to_generate)):
        nums_list.append(randint(0, max_value))

    with open('sample.txt', 'a') as my_file:
        for i in nums_list:
            my_file.write(str(i))
            my_file.write('\n')
    numbers_to_generate -= min(numbers_to_generate, numbers_each_loop)
    print(num,"/5")
    num += 1