grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
average = (grade1 + grade2) / 2

if average >= 7:
    status = "You have passed"
elif average >= 5 and average < 7:
    status = "You are in recovery"
else:
    status = "You have failed"
print(f'Your average is {average:.2f} and {status}')