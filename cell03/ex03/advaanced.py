import sys

# Check if the argument "yolo" is passed
if len(sys.argv) > 1 and sys.argv[1] == "yolo":
    print("none$")
    sys.exit()

# Define the outer loop for the tables 0 to 10
i = 0
while i <= 10:
    # Define the inner loop to generate the multiplication values for the current table
    j = 0
    result = []
    while j <= 10:
        result.append(str(i * j))  # Multiply and append the result to the list
        j += 1
    # Print the current multiplication table in the desired format
    print(f"Table de {i}: {' '.join(result)}")
    i += 1