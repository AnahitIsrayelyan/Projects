The problem is:
1. implement a program that will generate random numbers and store them in a file. File size is 4 GB
2. Sort the file using no more than 200 MB of RAM
3. get a file with no duplicate numbers
4. find the missing numbers in the resulting file and write them to another file

The solution is:
1. for sorting, divide the large file into smaller files, sort them separately, then merge them using merge-sort and save them in another file
2. when we already have the sorted file, we can read a certain range of numbers or two numbers each time, check if they are duplicates or not, and write only non-duplicates to the file
3. with the same logic as in the previous point, read numbers of a certain range, find the missing ones and write to the final file
