# Check if one of multiple strings exists in another string

my_str = 'apple, egg, avocado'
list_of_strings = ['apple', 'banana', 'kiwi']

if any(substring in my_str for substring in list_of_strings):
    # 👇️ this runs
    print('At least one of the multiple strings exists in the string')
else:
    print('None of the multiple strings exist in the string')