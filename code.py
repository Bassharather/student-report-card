def get_student_data(manual_input=True, predefined_data=None):
    student = {}

    if manual_input:
        student['name'] = input("Enter student name: ")
        student['roll_number'] = input("Enter roll number: ")
    else:
        student['name'] = predefined_data.get('name', 'Unknown')
        student['roll_number'] = predefined_data.get('roll_number', '000')

    subjects = ['Math', 'Physics', 'Urdu', 'English', 'Computer']
    marks = {}

    for subject in subjects:
        if manual_input:
            while True:
                try:
                    mark = float(input(f"Enter marks for {subject}: "))
                    if 0 <= mark <= 100:
                        marks[subject] = mark
                        break
                    else:
                        print("Marks should be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            marks[subject] = predefined_data.get(subject, 0)

    student['marks'] = marks
    return student


def calculate_percentage(marks):
    total_marks = sum(marks.values())
    percentage = (total_marks / (100 * len(marks))) * 100
    return percentage


def assign_grade(percentage):
    if percentage >= 80:
        return 'A+'
    elif percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'F'
    else:
        return 'F'


def display_report_card(students):
    print("\n\nStudent Report Cards")
    print("=" * 40)
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_number']}")
        print("Marks:")
        for subject, mark in student['marks'].items():
            print(f"  {subject}: {mark}")
        percentage = calculate_percentage(student['marks'])
        grade = assign_grade(percentage)
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print("-" * 40)


def main():
    students = []

    # Example predefined data for testing
    predefined_data = [
        {'name': 'John', 'roll_number': '001', 'Math': 80, 'Physics': 75, 'Urdu': 70, 'English': 85, 'Computer': 90},
        {'name': 'Alice', 'roll_number': '002', 'Math': 60, 'Physics': 65, 'Urdu': 50, 'English': 55, 'Computer': 70}
    ]

    # Uncomment the following lines for manual input mode
    # while True:
    #     student = get_student_data()
    #     students.append(student)
    #     more = input("Do you want to insert more records? (Y/N): ").strip().upper()
    #     if more != 'Y':
    #         break

    # For predefined data (useful for environments without input support)
    for data in predefined_data:
        students.append(get_student_data(manual_input=False, predefined_data=data))

    display_report_card(students)


if __name__ == "__main__":
    main()
