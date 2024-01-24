# Print the sum of the current number and the previous number

# Set the first number
current_number = 0

# Iterate for the first 10 numbers
for _ in range(10):
    # Print the sum of the current and previous number
    print(f"Current Number: {current_number}, Previous Number: {current_number - 1}, Sum: {current_number + (current_number - 1)}")
    
    # Update the current number for the next iteration
    current_number += 1