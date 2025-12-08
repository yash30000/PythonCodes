score = 0

q = input("Q1. Python is a programming language? (yes/no): ")
if q.lower() == "yes":
    score += 1

q = input("Q2. 5+5 = 10? (yes/no): ")
if q.lower() == "yes":
    score += 1

print("Your Score =", score)
