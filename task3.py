
def make_html_tags(*tags):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for tag in reversed (tags):
                print(tag, "tag is here ")
                result = f"<{tag}>{result}</{tag}>"
            return result
        return wrapper
    return decorator

# i shall consider the order of tag here 
# @make_html_tags("p", "em","strong") 
@make_html_tags("strong", "em", "p")
def get_custom_html_greeting(first, last):
    full_name = f"{first} {last}"
    return f"Hello, {full_name}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
