import keyword

def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False

# print(contains_keyword("hello", "goodbye"))
# print(contains_keyword("orca", "shark", "return"))
# print(contains_keyword("orca", "import"))

# import functions as fn

# print(fn.interleave("XOX","OXO"))