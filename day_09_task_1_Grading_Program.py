student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


# TODO-1: Create an empty dictionary called student_grades.
# TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}
for k, v in student_scores.items():
    if v >= 91 and v <= 100:
        student_grades[k] = "Outstanding"
    elif v >= 81 and v <= 90:
        student_grades[k] = "Exceeds Expectations"
    elif v >= 71 and v <= 80:
        student_grades[k] = "Acceptable"
    elif v < 70:
        student_grades[k] = "Fail"

print(student_grades)


student_grades1 = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades1[student] = "Outstanding"
    elif score > 80:
        student_grades1[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades1[student] = "Acceptable"
    elif score < 70:
        student_grades1[student] = "Fail"

print(student_grades1)
