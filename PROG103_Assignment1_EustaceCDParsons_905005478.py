# List to store student records
students = []


# Function to add a student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    # Input marks
    math = float(input("Enter Math score: "))
    english = float(input("Enter English score: "))
    science = float(input("Enter Science score: "))

    average = (math + english + science) / 3

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "id": student_id,
        "math": math,
        "english": english,
        "science": science,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No records found.\n")
        return

    # Loop through student list
    for student in students:
        print(f"Name: {student['name']}")
        print(f"ID: {student['id']}")
        print(f"Math: {student['math']}")
        print(f"English: {student['english']}")
        print(f"Science: {student['science']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print("------------------------")


# Main program loop
def main():
    while True:
        print("\n=== Student Record System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
main()
