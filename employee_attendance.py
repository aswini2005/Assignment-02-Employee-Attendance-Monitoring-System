excellent_count = 0
good_count = 0
improvement_count = 0
total_processed = 0

attendance_list = []

for employee in range(1, 11):

    attendance = float(input(f"Employee {employee} Attendance: "))

    if attendance == -1:
        print("Data entry stopped by user.")
        break

    if attendance == 0:
        print(f"Employee {employee}: Record skipped.")
        continue

    if attendance > 100:
        pass

    attendance_list.append(attendance)

    if attendance >= 90:
        category = "Excellent"
        excellent_count += 1

    elif attendance >= 75:
        category = "Good"
        good_count += 1

    else:
        category = "Improvement Required"
        improvement_count += 1

    print(f"Employee {employee} : {category}")

    total_processed += 1

print("\nAttendance Summary")
print("----------------------")
print("Total Employees Processed :", total_processed)
print("Excellent :", excellent_count)
print("Good :", good_count)
print("Improvement Required :", improvement_count)

print("Bonus task")

if total_processed > 0:
    highest_attendance = max(attendance_list)
    lowest_attendance = min(attendance_list)
    average_attendance = sum(attendance_list) / total_processed

    excellent_percentage = (excellent_count / total_processed) * 100
    good_percentage = (good_count / total_processed) * 100
    improvement_percentage = (improvement_count / total_processed) * 100

    print("\nAdditional Insights")
    print("Highest Attendance Percentage :", highest_attendance)
    print("Lowest Attendance Percentage :", lowest_attendance)
    print("Average Attendance Percentage :", round(average_attendance, 2))

    print("\nCategory Distribution")
    print("Excellent Percentage :", round(excellent_percentage, 2), "%")
    print("Good Percentage :", round(good_percentage, 2), "%")
    print("Improvement Required Percentage :", round(improvement_percentage, 2), "%")