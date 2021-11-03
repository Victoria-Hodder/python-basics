
"""
Items of universities list:
1. The name of a university
2. The total number of enrolled students
3. The annual tuition fees
"""

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

# List the names of the universities
# for item in universities:
#     print(item[0])

"""
enrollment_stats() should return two lists, the first containing all the
student enrollment values and the second containing all the tuition
fees.
"""

def enrollment_stats(universities):
    student_enrollments = [item[1] for item in universities]
    tuition_fees = [item[2] for item in universities]
    return student_enrollments, tuition_fees

# Tuple unpacking
student_enrollments, tuition_fees = enrollment_stats(universities)

print(f"Student enrollments: {student_enrollments}")
print(f"Tuition fees: {tuition_fees}")
