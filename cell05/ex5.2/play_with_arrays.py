# play_with_arrays.py

# Original array
arr = [2, 8, 9, 48, 8, 22, -12, 2]

# Filter values greater than 5
filtered_arr = [x for x in arr if x > 5]

# Process the filtered array (for example, multiplying each value by 2)
processed_arr = [x * 2 for x in filtered_arr]

# Print the result (similar to the example output)
print(processed_arr)