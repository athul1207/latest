import sys

# Check if the required arguments are passed
if len(sys.argv) != 3:
    print("Usage: python ratio.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    
    # Your ratio calculation logic here
    ratio = num1 / num2
    print(f"The ratio of {num1} to {num2} is {ratio}")
except ValueError:
    print("Please enter valid numbers.")
