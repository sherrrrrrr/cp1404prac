import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# A: The random integer between 5 and 20, including both 5 and 20.

# What was the smallest number you could have seen, what was the largest?
# A: The smallest number is 5 and the largest number is 20 in the specified range.
# Smallest: 5, Largest: 20

# What did you see on line 2?
# A: The random number picked from the range [3, 10) with a step of 2 (inclusive for start, exclusive for stop).

# What was the smallest number you could have seen, what was the largest?
# A: The smallest number is 3 and the largest number is 9 in the specified range.
# Smallest: 3, Largest: 9

# Could line 2 have produced a 4?
# A: No, because the step size is 2, so the numbers generated will be odd.

# What did you see on line 3?
# A: The random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# A: The smallest number is 2.5 and the largest number is 5.5 in the specified range.
# Smallest: 2.5, Largest: 5.5

# Write code to produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
