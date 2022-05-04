student_scores = list(map(int,\
    input("Please enter scores that you want calculate. :")\
    .split(", ")))
max = 0    
for score in student_scores:
    if (score > max):
        max = score
print("The highest score in the class is {0}".format(max))
