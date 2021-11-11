
def enrollment_stats(universities):
    """
    Returns two lists, the first containing all the student enrollment
    values and the second containing all the tuition fees.
    """
    student_enrollments = [item[1] for item in universities]
    tuition_fees = [item[2] for item in universities]
    return student_enrollments, tuition_fees

def calculate_mean(list_of_numbers):
    """
    Returns the mean of a given list of integers
    """
    mean_num = sum(list_of_numbers) / len(list_of_numbers)
    return mean_num

def calculate_median(list_of_numbers):
    """
    Returns the median of a given list of integers
    """
    list_of_numbers = sorted(list_of_numbers)

    # Find if length of list even or odd
    if len(list_of_numbers) % 2 == 0:
        # Use indices to find middle numbers
        left_center_index = (len(list_of_numbers) // 2) - 1
        right_center_index = len(list_of_numbers) // 2
        # Calculate median by adding the two middle numbers and dividing by 2
        median_num = (list_of_numbers[left_center_index] + list_of_numbers[right_center_index]) // 2
        return median_num
    else:
        center_index = int(len(list_of_numbers) / 2)
        median_num = list_of_numbers[center_index]
        return median_num

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
Unpack tuples to assign student_enrollments and tuition_fees
to separate variables
"""
student_enrollments, tuition_fees = enrollment_stats(universities)

print(30 * '*')

print(f"Student total: {sum(student_enrollments):,}")
print(f"Tuition total: $ {sum(tuition_fees):,}\n")

print(f"Student mean: {calculate_mean(student_enrollments):,.2f}")
print(f"Student median: {calculate_median(student_enrollments):,}\n")

print(f"Tuition mean: $ {calculate_mean(tuition_fees):,.2f}")
print(f"Tuition median: $ {calculate_median(tuition_fees):,}")

print(30 * '*')
