student_heights = input("Input a list od student height: ").split()
print(student_heights)

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # print(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
# print(average_height)


# total_height = 0
# number_of_students = 0
# for height in student_heights:
#     total_height += height
#     number_of_students += 1
# print(total_height)
# print(number_of_students)
# print(round(total_height/number_of_students))


total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += height
    number_of_students += 1
    average = round(total_height/number_of_students)
print(total_height)
print(number_of_students)
print(average)
