customers = {  # dictionaries use {}. Case sensitive. Can only have one key per; no repeats.
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customers["name"] = "Jack Smith"  # you can declare a new value in a dictionary
customers["email"] = "john@gmial.com"
print(customers.get("birthdate"))  # if you pass a nonexistent key it returns none
print(customers.get("birthdate", "Jan 1st 1980"))  # you can provide it a value
print(customers["email"])

# Practice
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)