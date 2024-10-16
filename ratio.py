# Function to calculate ratio
def calculate_ratio(num1, num2):
    if num2 == 0:
        return "Ratio cannot be calculated because division by zero is not allowed."
    ratio = num1 / num2
    return ratio

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and print the ratio
result = calculate_ratio(num1, num2)
print(f"The ratio of {num1} to {num2} is: {result}")
