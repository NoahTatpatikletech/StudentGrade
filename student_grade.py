import sys


def calculate_grade(avg):
  if 90 <= avg <= 100:
    return "S"
  elif 80 <= avg <= 89:
    return "A"
  elif 65 <= avg <= 79:
    return "B"
  elif 50 <= avg <= 64:
    return "C"
  elif 40 <= avg <= 49:
    return "D"
  else:
    return "F"


if len(sys.argv) == 7:
  name = sys.argv[1]
  department = sys.argv[2]
  semester = sys.argv[3]
  m1 = float(sys.argv[4])
  m2 = float(sys.argv[5])
  m3 = float(sys.argv[6])
else:
  name = input("Enter Student Name: ")
  department = input("Enter Department: ")
  semester = input("Enter Semester: ")
  m1 = float(input("Enter Marks for Subject 1: "))
  m2 = float(input("Enter Marks for Subject 2: "))
  m3 = float(input("Enter Marks for Subject 3: "))

average = (m1 + m2 + m3) / 3
grade = calculate_grade(average)

print("\n--- Student Result ---")
print("Name       :", name)
print("Department :", department)
print("Semester   :", semester)
print(f"Average    : {average:.2f}")
print("Grade      :", grade)