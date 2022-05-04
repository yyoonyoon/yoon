student_heights = list(map(int,input("Input a list if student heights. :")\
    .split(", ")))
total = 0
for student in student_heights:
    total = total + student

print(round(total/len(student_heights)))
