
import statistics

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

# print(f"Student enrollments: {student_enrollments}")
# print(f"Tuition fees: {tuition_fees}")

def calculate_mean(list_of_numbers):
    mean_sum = sum(list_of_numbers) / len(list_of_numbers)
    return round(mean_sum, 2)

print(f"Student mean: {calculate_mean(student_enrollments)}")
print(f"Tuition mean: {calculate_mean(tuition_fees)}")

def calculate_median(list_of_numbers):
    median_number = statistics.median(list_of_numbers)
    return median_number

print(f"Student median: {calculate_median(student_enrollments)}")
print(f"Tuition median: {calculate_median(tuition_fees)}")
