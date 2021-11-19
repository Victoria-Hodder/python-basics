
import statistics

# odd
# total_students = [2175, 19627, 10566, 7802, 5879, 19535, 11701]
# even
total_students = [2175, 19627, 10566, 7802, 5879, 19535, 11701, 7456]

# sort list!
total_students = sorted(total_students)
# print(total_students)

# Find if length of list even or odd
if len(total_students) % 2 == 0:
    # Use indices to find middle numbers
    idx_1 = int(len(total_students) / 2)
    idx_2 = int((len(total_students) / 2) - 1)
    # Calculate median by adding the two middle numbers and dividing by 2
    median = int((total_students[idx_1] + total_students[idx_2]) / 2)
    print(f"The median is: {median}")
else:
    idx = int((len(total_students) / 2) - 0.5)
    median = total_students[idx]
    print(f"The median is: {median}")


# Use statistics module for double checking answer
# print(statistics.median(total_students))
