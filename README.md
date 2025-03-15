# Student Report Card Generator

## Project Description
The **Student Report Card Generator** is a Python program designed to collect student data, calculate percentages, and assign grades based on the marks obtained in five subjects: Math, Physics, Urdu, English, and Computer. The program generates a detailed report card for each student.

## Features
- **Data Input**: Supports both manual input and predefined data for testing purposes.
- **Error Handling**: Ensures only numeric input between 0 and 100 is accepted.
- **Grade Calculation**: Calculates the percentage and assigns a grade based on the following criteria:
  - 80% and above: Grade A+
  - 70% to 79%: Grade A
  - 60% to 69%: Grade B
  - 50% to 59%: Grade C
  - 40% to 49%: Grade F
  - Below 40%: Grade F
- **Report Generation**: Displays the report card with marks, percentage, and grade for each student.
- **Flexible Input Mode**: Allows switching between manual input and predefined data for batch processing.

## How to Run the Program
1. Clone the repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd student-report-card
```

3. Run the program:

```bash
python reportcard.py
```

4. For manual input mode, uncomment the lines in the `main()` function that handle manual input.

## Technologies Used
- Python 3.x

## Future Improvements
- Add functionality to export report cards as PDF or CSV.
- Implement a GUI for better user interaction.

## Author
Bassharather