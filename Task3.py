# Create a grading system: Take input marks (0-100) and display grades like A, B, C, D, or Fail based on defined ranges.

marks = int(input("Enter the mark : "))

if marks>90:
    print("A")
elif marks<=90 and marks>80:
    print("B")
elif marks<=80 and marks>70:
    print("C")
elif marks<=70 and marks>60:
    print("D")
else:
    print("F")
