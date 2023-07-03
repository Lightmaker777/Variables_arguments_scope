#Task 3: Default and non default arguments combined
# Define the global variables with the 'pages' key
settings = {'title': 'My original title', 'pages': []}
default_settings = {'title': 'My original title', 'pages': []}


def change_site_title(new_title):    
    global settings
    settings['title'] = new_title

def get_title(dictionary=default_settings):    
    return dictionary['title']

def get_pages(settings=default_settings):    
    return settings['pages']

def add_page(page, settings=default_settings):    
    settings['pages'].append(page)


home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))
