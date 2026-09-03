# Complete the if and elif statements!
def grade_converter(grade: int) -> str:
    if grade_converter(grade:int) > 90:
        return "A"
    elif grade_converter(grade: int) >=80 :
        return "B"
    elif grade_converter(grade: int) >=70:
        return "C"
    elif grade_converter(grade: int) >= 65:
        return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))
