#gracie oxnam
#functions practice - string, tuple, set, array

import random

def make_random_list (num, range_start, range_end):
    #returns a list filled with random numbers between start/end
    r_list = []
    for i in range (num):
        new = random.randint(range_start,range_end)
        r_list.append(new)
    return (r_list)    

def ask_for_list ():
    num = int(input("How many numbers do you want to print: "))
    range_start = int(input("Where does the list start: "))
    range_end = int(input("Where does the list end: "))
    return make_random_list(num, range_start, range_end)
                 

make_random_list (23, 1, 365)

ask_for_list()
