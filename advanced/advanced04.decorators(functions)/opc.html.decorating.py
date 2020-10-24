# opc.html.decorating.py
# source (mod): https://gist.github.com/Zearin/2f40b7b9cfc51132851a


# The decorator to make it bold
def makebold(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return '<b>' + fn() + '</b>'
    return wrapper

# The decorator to make it italic
def makeitalic(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return '<i>' + fn() + '</i>'
    return wrapper

@makebold
@makeitalic
def say():
    return 'hello'

print(say())
