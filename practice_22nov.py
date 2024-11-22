#gracie oxnam
#stings practice

#print (str[0]+str[:1]+str[:2]+str[:4]+str[:5]) #WORKS BUT ONLY UP TO 5
def string_splosion(str):
    #returns an exploded version of a string given
    exploded = ""
    for i in range(len(str)):
        exploded += str[:i]
    return (exploded+str)
    
print(string_splosion("hello"))
print(string_splosion("code"))
print(string_splosion("abc"))

#-----------------------------------------------------------------------

students = ["gracie", "joao", "hayden", "gregan", "jackson", "matthew"]
grades = [3.5, 4.0, 2.75, 100, 3.75, 3.0]

students.append("ronan")
grades.append(20)

#into one dictornary
    #cannot change the order --> fixed order
    #cannot insert - only adding to the end
student_grades = {"gracie":3.5,"joao":4.0,"hayden":2.75,"gregan":3.75,"jackson":3.75}
