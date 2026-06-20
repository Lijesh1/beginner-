def student_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # student details
    print("Student Report ")
    print(f"Student Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")

    # Check for subjects with marks below 40
    print("Subjects with marks below 40:")
    for i, mark in enumerate(marks, start=1):
        if mark < 40:
            print(f"  Subject {i}: {mark}")


name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)


student_result(name, roll, marks)
