#gracieoxnam
#learning dictonaries
# collection data types

def in1020 (a,b):
    #take two numbers and returns true is inbetween 10-20
    if a > 10 and a < 20:
        return True
    elif b > 10 and b < 20:
        return True
    #otherwise false
    else:
        return False

def not_string (str):
    #returns a string that has 'not' in front of orginal
    #check if "not" starts the string and reurn as is
    str = []
    print (str)
    if (str [0]) == "not":
        return str
    #if 'not' is already there return sting as is
    else:
        return ("Not" + str)

print (in1020(1,4))
#print (not_string ("going to get the dog"))

#DICTONARY PRACTICE
alien = {"home planet": "Mars",
         "skin color": "green",
         "age": 90,
         "number of eyes": 90,
         "fingers": "10 each hand",
         "languages spoken":["spanish", "czech", "dutch", "klingon"]}
print(alien["age"])
print(alien.items())
#print(alien["languages spoken"[2]])

for key in alien.keys():
    print(alien[key])
for item in alien.items():
    print (item)
for key, value in alien.items(): #unpacking with tuple
    print(key,value)
