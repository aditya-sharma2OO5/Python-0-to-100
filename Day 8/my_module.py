# Custom module made for Day 8.
# Keep module file in the same directory as the files where you want to import this module, so importing becomes easier.

print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    """Find the index of a value in a sequence"""

    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1