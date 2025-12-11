m1 = int(input("Enter Marks1: "))
m2 = int(input("Enter Marks2: "))
m3 = int(input("Enter Marks3: "))

avg = (m1+m2+m3)/3

if avg >= 90: grade = "A"
elif avg >= 75: grade = "B"
elif avg >= 60: grade = "C"
else: grade = "D"

print("Average:", avg)
print("Grade:", grade)
