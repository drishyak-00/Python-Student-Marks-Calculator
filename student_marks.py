print("STUDENT MARKS CALCULATOR")

name = input("Enter student name: ")

mark1 = int(input("Enter mark for English: "))
mark2 = int(input("Enter mark for Maths: "))
mark3 = int(input("Enter mark for Science: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")