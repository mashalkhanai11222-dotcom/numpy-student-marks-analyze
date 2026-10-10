
import numpy as np

marks = np.array([1, 23, 56, 78, 90, 87, 90, 76, 90, 76, 97])

print("\n===== STUDENT MARKS ANALYZER =====")
print("1. Show Marks")
print("2. Total Marks")
print("3. Average Marks")
print("4. Highest Marks")
print("5. Lowest Marks")
print("6. Passed and Failed")
print("7. Show Grade")
print("8. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Marks:", marks)

elif choice == 2:
    print("Total Marks:", np.sum(marks))

elif choice == 3:
    print("Average Marks:", np.mean(marks))

elif choice == 4:
    print("Highest Marks:", np.max(marks))

elif choice == 5:
    print("Lowest Marks:", np.min(marks))

elif choice == 6:
    print("Passed:", np.sum(marks >= 50))
    print("Failed:", np.sum(marks < 50))

elif choice == 7:
    average = np.mean(marks)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

elif choice == 8:
    print("Program closed!")

else:
    print("Invalid choice! Please enter 1 to 8.")
