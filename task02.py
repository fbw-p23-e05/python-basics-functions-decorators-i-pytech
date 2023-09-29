def get_html_greeting():
    return 'Hello, World!'

def make_bold(func):
    def inner():
        print('<strong>'+ func()+ '</strong>')
    return inner

def get_custom_html_greeting(first, last):
    return first, last

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())