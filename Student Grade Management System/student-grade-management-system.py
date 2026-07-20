students = []


def calculate_average(grades):
    total = sum(grades.values())
    number_of_subjects = len(grades)

    average = total / number_of_subjects

    return average


def calculate_grade(average):

    if average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def add_student():

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    mathematics = float(input("Enter Mathematics score: "))
    english = float(input("Enter English score: "))
    science = float(input("Enter Science score: "))

    grades = {
        "Mathematics": mathematics,
        "English": english,
        "Science": science
    }

    student = {
        "name": name,
        "id": student_id,
        "grades": grades
    }

    students.append(student)

    print("Student added successfully!\n")


def view_students():

    if len(students) == 0:
        print("No students available.\n")

    else:

        for student in students:

            average = calculate_average(student["grades"])
            grade = calculate_grade(average)

            print(f"Name: {student['name']}")
            print(f"Student ID: {student['id']}")

            print("\nGrades:")

            for subject, score in student["grades"].items():
                print(f"{subject}: {score}")

            print(f"\nAverage: {average:.2f}")
            print(f"Grade: {grade}")

            print("-" * 30)
