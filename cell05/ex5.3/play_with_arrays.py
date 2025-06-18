# play_with_arrays.py

# Original array
arr = [2, 8, 9, 48, 8, 22, -12, 2]

# Filter values greater than 5 and convert to a set to remove duplicates
filtered_set = {x for x in arr if x > 5}

# Process the filtered set (for example, multiplying each value by 2)
processed_set = {x * 2 for x in filtered_set}

# Print the result (similar to the example output)
print(str(sorted(processed_set)) + "$")