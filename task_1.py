#Task 1

#Define a global variable named settings as a dictionary with a key title that contains a string of your choice, then create a function named change_site_title that takes one argument of type String and assigns it to the key title in the global variable settings.

settings = {'title': "What a beautiful wether!"}

def change_site_title(new_title):
    global settings
    settings['title'] = new_title

print(settings)
change_site_title("A new fancy title")
print(settings)