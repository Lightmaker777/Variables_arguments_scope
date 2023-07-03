#Task 2

#Keeping the previous code and defining now a global variable named default_settings as a dictionary with a key title, then creating a function named get_title that takes one argument as a dictionary that defaults to default_settings and returns the content of the key title in the given dictionary.


settings = {'title': 'Hi Everyone!'}
default_settings = {'title': 'Great Work!'}
def change_site_title(new_title):    
    global settings
    settings['title'] = new_title

def get_title(dictionary=default_settings):
    
    return dictionary['title']

print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())


