#Create a dictionary with roll numbers as keys and student names as values.

# Add a function to search for a name using roll number.

students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "Diana"
}


def search_student(roll_number):
    if roll_number in students:
        print(f"Student found: {students[roll_number]}")
    else:
        print("Student not found.")

# Example
search_student(102)
search_student(105)