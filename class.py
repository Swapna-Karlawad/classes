classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
attendance_percentage = (classes_attended / classes_held) * 100
print("Attendance Percentage:", attendance_percentage, "%")
if attendance_percentage >= 75:
    print("You are allowed to write the exam.")
else:
    print("You are not allowed to write the exam.")