#Task 4:
#Create a new function named print_user_profile that will take 4 parameters

def print_user_profile(gender='female', first='', last='Doe', pictures=[]):
    """
    Print the user profile information including the common header picture and list of pictures.
    
    Arguments:
    - gender: A string indicating the gender of the user. Available values: 'male', 'female'. Default: 'female'.
    - first: A string with the first name of the user. Default: 'John' for male, 'Jane' for female.
    - last: A string with the last name of the user. Default: 'Doe'.
    - pictures: A list of strings with the names of the picture files. Default: empty list.
    """
    header_picture = 'common_header.png'
    if not first:
        first = 'John' if gender == 'male' else 'Jane'
    print(f"The user {first} {last} has the following pictures:")
    print(header_picture)
    for picture in pictures:
        print(picture)

# Test cases
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}

print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)
