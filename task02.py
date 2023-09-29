def make_bold(func):
    def inner(first='Hello', last='World'):
        return f'<strong>{func(first, last)}</strong>'
    return inner

@make_bold
def get_html_greeting(word1, word2):
    return f'{word1}, {word2}!'

@make_bold
def get_custom_html_greeting(first, last):
    return f'Hello, {first} {last}!'

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())