"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A. A ValueError will occur if the input provided for numerator or
   denominator cannot be converted to an integer.
2. When will a ZeroDivisionError occur?
A. When the denominator is 0, this operation does not exist.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
A. Yes, in order to avoid generating ZeroDivisionError, we can check whether the denominator
of the data is zero before dividing. If the denominator is zero, we can treat it alone.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
