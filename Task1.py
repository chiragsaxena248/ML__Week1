#Store marks of 3 students in 3 subjects in a matrix format.

#Calculate total and average marks for each student.

marks = [
    [24,26,28],
    [26,25,28],
    [25,27,29]
    ]

for i in range(3):
    total = sum(marks[i]) # function sum is used 
    average = total / len(marks[i])
    print(f"Student {i+1}: Total = {total}, Average = {average:.2f}")


