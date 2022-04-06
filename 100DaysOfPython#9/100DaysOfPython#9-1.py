student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for key, scores in student_scores.items():
    if (91 <= scores <= 100):
        student_grades[key] = "Outstanding"
    elif (81 <= scores <= 90):
        student_grades[key] = "Exceeds Expectations"
    elif (71 <= scores <= 90):
        student_grades[key] = "Acceptable"
    else:    
        student_grades[key] = "Fail"

print(student_grades)