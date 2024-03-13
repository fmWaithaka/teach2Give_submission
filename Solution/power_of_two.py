# Write a program that takes an integer as input and returns true if the input is a power of two.

# Examples:
# 8=> returns true
# 6=> returns false


def power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def test_power_of_two():
    assert power_of_two(6) == False
    assert power_of_two(8) == True
    assert power_of_two(5) == False
    assert power_of_two(128) == True


print(test_power_of_two()) # returns None
print(power_of_two(6)) # returns false
print(power_of_two(8)) # returns true
print(power_of_two(5)) # returns false
print(power_of_two(128)) # returns true