# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Using elif statement
# Determine the grade.
if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')

# Using "switch" statement
# Determine the grade.
# Using "match-case" statement determining the grade.
match score:
    case _ if score >= A_score:
        print('Your grade is A.')
    case _ if score >= B_score:
        print('Your grade is B.')
    case _ if score >= C_score:
        print('Your grade is C.')
    case _ if score >= D_score:
        print('Your grade is D.')
    case _:
        print('Your grade is F.')
