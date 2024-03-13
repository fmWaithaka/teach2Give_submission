# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.
# Examples:

# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize(s):
    return s.title()

def test_capitalize():
    assert capitalize("hi") == "Hi"
    assert capitalize("i love programming") == "I Love Programming"

print(test_capitalize()) # returns None
print(capitalize("i love programming")) # returns "I Love Programming"