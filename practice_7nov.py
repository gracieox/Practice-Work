#gracie oxnam
#True/False Parameters
#function practice
#athrithmatic, relational, logical ('and' before 'or'), uninary, binary
#(),-,not,**,*,/,//,%,+,-,<,>,<=,>=,==,:=,and,or


def check_within_ten(num):
    #I need to compare num with 100
    if num == 100:
        return ("true")
    #If num -100 in between 0 and 10
    if (num-100 <= 10) and (num-100 >= -10):
        within_ten = True
    #It is within 10 of 100
    #Or if num -100 is inbetween 0 and -10
    #It is within 10 of 100
    else:
        within_ten = False
    #have to end with a return
    return within_ten


def check_within_ten(num):
    if num<=110 and num>=90:
        return "True"
    else:
        return "False"

within_ten = False #allows so that you aready created within_ten
def check_within_ten(num):
    if (num-100 <= 10) and (num-100 >= -10):
        return True
    else:
         return False

def check_within_ten (num):
    return (10>= num-100) and (num - 100 >= -10)


print(check_within_ten(73))
print(check_within_ten(95))
print(check_within_ten(103))
print(check_within_ten(117))
