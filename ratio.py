import sys

# Check if the required arguments are passed
if len(sys.argv) < 3:
    print("Usage: python ratio.py <num1> <num2>")
    sys.exit(1)

# Read the command-line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# Calculate the ratio
ratio = num1 / num2

# Print the result
print(f"The ratio of {num1} to {num2} is {ratio:.2f}")

