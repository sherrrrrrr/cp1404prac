is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        break  # Exit the loop if a valid integer is entered
    except ValueError:  # Specify the exception to catch
        print("Please enter a valid integer.")

print("Valid result is:", result)