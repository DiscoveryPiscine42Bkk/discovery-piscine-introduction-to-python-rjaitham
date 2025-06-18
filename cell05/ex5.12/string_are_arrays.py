import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    for char in input_string:
        if char == 'z':
            print('z')