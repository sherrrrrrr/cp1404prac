user_name = input("Please enter your name: ")
with open("name.txt", "w") as file:
    file.write(user_name)

with open("name.txt", "r") as file:
    name = file.read().strip()
    print(f"Your name is {name}")

with open("numbers.txt", "r") as file:
    numbers = file.readlines()
    sum_first_two = int(numbers[0]) + int(numbers[1])
    print(f"Sum of the first two numbers is: {sum_first_two}")

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(f"Total of all numbers in the file is: {total}")