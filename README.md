# Assignment-02-Employee-Attendance-Monitoring-System
# Employee Attendance Classification System

## Overview

This Python program records employee attendance percentages, classifies employees based on attendance performance, and generates a summary report with additional insights.

The project demonstrates the use of:

* `for` loops
* `if-elif-else` statements
* `break`
* `continue`
* `pass`
* Lists
* Counters and statistics

---

## Features

### Attendance Classification

Employees are categorized based on attendance percentage:

| Attendance Percentage | Category             |
| --------------------- | -------------------- |
| 90% and above         | Excellent            |
| 75% to 89.99%         | Good                 |
| Below 75%             | Improvement Required |

---

### Loop Control Statements

#### `break`

Entering `-1` stops the data entry process immediately.

Example:

```text
Employee 5 Attendance: -1
Data entry stopped by user.
```

#### `continue`

Entering `0` skips the current employee record without processing it.

Example:

```text
Employee 3 Attendance: 0
Employee 3: Record skipped.
```

#### `pass`

If attendance exceeds `100`, the program executes `pass` as a placeholder for future validation logic.

---

## Additional Insights Generated

After processing employee records, the program calculates:

* Highest Attendance Percentage
* Lowest Attendance Percentage
* Average Attendance Percentage
* Percentage of Employees in each category

---

## Example Output

```text
Employee 1 Attendance: 95
Employee 1 : Excellent

Employee 2 Attendance: 82
Employee 2 : Good

Employee 3 Attendance: 70
Employee 3 : Improvement Required

Employee 4 Attendance: 0
Employee 4: Record skipped.

Employee 5 Attendance: -1
Data entry stopped by user.

Attendance Summary
----------------------
Total Employees Processed : 3
Excellent : 1
Good : 1
Improvement Required : 1

Additional Insights
Highest Attendance Percentage : 95.0
Lowest Attendance Percentage : 70.0
Average Attendance Percentage : 82.33

Category Distribution
Excellent Percentage : 33.33 %
Good Percentage : 33.33 %
Improvement Required Percentage : 33.33 %
```

---

## How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd employee-attendance-system
   ```

3. Run the program:

   ```bash
   python attendance.py
   ```

---

## Project Structure

```text
employee-attendance-system/
│
├── attendance.py
└── README.md
```

---

## Learning Outcomes

This project helps beginners understand:

* Python loops
* Conditional statements
* Loop control statements
* List operations
* Statistical calculations
* Basic data processing

---

## License

This project is open-source and available for educational purposes.
