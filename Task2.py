#Store each student’s data as a tuple: (roll_number, name, age).

# Display the student info neatly.

students = [
    (101, "Alice", 20),
    (102, "Bob", 21),
    (103, "Charlie", 19),
    (104, "Diana", 22)
]


print(f"{'Roll No.':<10}{'Name':<15}{'Age':<5}")
print("-" * 30)

for student in students:
    roll_number, name, age = student
    print(f"{roll_number:<10}{name:<15}{age:<5}")