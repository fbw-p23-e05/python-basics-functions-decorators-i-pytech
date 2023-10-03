
def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper

@make_bold
def get_html_greeting():
    return "Hello, World!"

@make_bold
def get_custom_html_greeting(first, last):
    return f"Hello, {first} {last}!"

@make_bold
def get_html_greeting(name, age):
    return {"message": f"Hello, {name} your age: {age}"}

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(last="Brown",first="James"))
print(get_html_greeting(name="Alex", age=30))
