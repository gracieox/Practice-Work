#gracie oxnam
#function practice

def unique_squares(nums):
    squared = []
    for num in nums:
        if (num*num) not in squared:
            squared.append(num*num)
    return squared

#return (int(input(list_nums))**2)
#def unique_squares_but_bad(nums):
    #return [num*num for num in set(nums)]

unique_squares ([2,7,13,9])
unique_squares ([2,11,2,7])

         #for i in range (n):
            #nums[i] *= nums[i]
#gives user acess to your list, may help keep values
        #for item in list:
#cleaner, no user can gain acess
