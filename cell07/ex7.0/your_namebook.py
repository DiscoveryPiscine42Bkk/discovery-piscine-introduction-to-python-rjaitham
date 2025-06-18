def array_of_names(names_dict):
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in names_dict.items()]

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))