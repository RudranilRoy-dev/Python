class MarksOutOfRangeError(Exception):
    pass
try:
    marks = int(input("Enter marks (0 to 100): "))
    if marks > 100:
        raise MarksOutOfRangeError("Marks cannot be greater than 100!")
    print("Marks entered:", marks)
except MarksOutOfRangeError as e:
    print("Error:", e)
