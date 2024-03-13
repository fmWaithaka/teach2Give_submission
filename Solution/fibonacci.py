# Write a program to generate the Fibonacci sequence up to 100.
# Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

def fibonacci():
    fib = [0, 1]
    while fib[-1] + fib[-2] <= 100:  
        fib.append(fib[-1] + fib[-2])
    return fib

def test_fibonacci():
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
    actual_sequence = fibonacci()
    assert actual_sequence == expected_sequence, f"Expected: {expected_sequence}, Actual: {actual_sequence}"

test_fibonacci()  # raise AssertionError if the test fails
print(fibonacci())
