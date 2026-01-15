# WAP TO CHECK IF THE STUDENT IS PASS OR FAIL
# 1      MARKS>= 90, GRADE "A"
# 2 90 > MARKS >= 80, GRADE "B"
# 3 80 > MARKS >= 70, GRADE "C"
# 4 70 > MARKS GRADE "D"

marks = int(input("Please enter your marks : ")) #we have to use typeCasting because python takes input as a string form.
if(marks >= 90):
    print("congratulation you got grade 'A'")
elif(marks >= 80 and marks<90):
    print("congratulation you got grade 'B'")
elif(marks >= 70 and marks<80):
    print("congratulation you got grade 'C'") 
else:
    print("you got grade 'D'")
