#gracie oxnam
#intorduction to tuples

#individual work
def find_max (a,b):
     if find_max[a] < find_max[b]:
         print(find_max[b])
     else:
         print (find_max[a])
         
#together with class
 def find_max (a,b):
        if a > b:
            return a
        return b
num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
find_max(a,b)

if num1 > num2:
    print(f"{num1} is larger")
else:
    print(f"{num2} is larger (or they are equal)")

#learning tuples
def return_top_two(a,b,c):
    temp = [a,b,c]
    sort(temp)
    return temp[1], temp[2]

next_best, best = return_top_two (5, 78, 2)
top = return_top_two(3245, 56, 1333525464)
