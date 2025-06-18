arr = [2, 8, 9, 48, 8, 22, -12, 2]

filtered_arr = [x for x in arr if x > 5]

processed_arr = [x * 2 for x in filtered_arr]

print(processed_arr)