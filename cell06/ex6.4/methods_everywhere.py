import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + 'Z' * (8 - len(text)))

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) < 8:
            enlarge(arg)
        elif len(arg) > 8:
            shrink(arg)
        else:
            print(arg)

