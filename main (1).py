print("====================================")
print("   PERSONAL POCKET CGPA CALCULATOR")
print("====================================")

total_courses = int(input("Enter the number of courses: "))

total_grade_points = 0
total_credit_units = 0

for i in range(1, total_courses + 1):
    print(f"\nCourse {i}")

    credit_unit = int(input("Enter Credit Unit: "))
    score = float(input("Enter Score (0-100): "))

    if score >= 70:
        grade_point = 5
        grade = "A"
    elif score >= 60:
        grade_point = 4
        grade = "B"
    elif score >= 50:
        grade_point = 3
        grade = "C"
    elif score >= 45:
        grade_point = 2
        grade = "D"
    elif score >= 40:
        grade_point = 1
        grade = "E"
    else:
        grade_point = 0
        grade = "F"

    print("Grade:", grade)

    total_grade_points += grade_point * credit_unit
    total_credit_units += credit_unit

cgpa = total_grade_points / total_credit_units

print("\n====================================")
print("Your CGPA is:", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
else:
    print("Class of Degree: Pass")