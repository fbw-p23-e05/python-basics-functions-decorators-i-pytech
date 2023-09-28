
def make_bold(func):
    def wrapper():
        result = func()
        return f"<strong>{result}</strong>"
    return wrapper
