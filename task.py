# Function to calculate percentage
def calculate_percentage(number, total):
    if total == 0:
        return "Total cannot be zero."
    percentage = (number / total) * 100
    return percentage

# Input from the user
number = float(input("Enter the number: "))
total = float(input("Enter the total value: "))

# Calculate and print the percentage
result = calculate_percentage(number, total)
print(f"The percentage is: {result}%")
