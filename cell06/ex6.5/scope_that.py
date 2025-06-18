def add_one(number):
    return number + 1

if __name__ == "__main__":
    number = 42
    print("Before:", number)
    number = add_one(number)
    print("After:", number)