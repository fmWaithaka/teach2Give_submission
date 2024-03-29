# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.
# Examples:

# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

def reverse_integer(n):
    return int(str(n)[::-1]) if n > 0 else -int(str(-n)[::-1])

def test_reverse_integer():
    assert reverse_integer(500) == 5
    assert reverse_integer(-56) == -65
    assert reverse_integer(-90) == -9
    assert reverse_integer(91) == 19

print(test_reverse_integer()) # returns None
print(reverse_integer(500)) # returns 5
print(reverse_integer(-56)) # returns -65
print(reverse_integer(-90)) # returns -9
print(reverse_integer(91)) # returns 19