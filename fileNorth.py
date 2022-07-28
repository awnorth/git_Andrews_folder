# Hi Em

A = 5
B = 7

C = A+B
print(C)

# What time is bed?
def bedtime(tired_level):
    if tired_level < 5:
        return "Bed Time is 12:30am"
    elif tired_level < 7:
        return "Bed Time is 12:00am"
    elif tired_level < 9:
        return "Bed Time is 11:00pm"
    else:
        return "Bed Time is NOW!"

tired_level = int(input("What is your tired level on a scale between 1-10?:"))

print(bedtime(tired_level))

