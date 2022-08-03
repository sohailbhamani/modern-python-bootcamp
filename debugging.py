# pdb usage to set a trace and allow stepping through lines
# import pdb
#
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

# More standard usage with importing and set trace on one line when needed.  This line is temporary and would never
# ship with completed code
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()

    return a + b + c + d

print(add_numbers(1,2,3,4))
