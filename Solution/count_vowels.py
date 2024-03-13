# Write a program that counts the number of vowels in a sentence.

# eg " Hello World " => returns 2


def count_vowels(s):
    return sum([1 for i in s if i in 'aeiouAEIOU'])

def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Hi") == 1
    assert count_vowels("I love programming") == 6
    assert count_vowels("I Love Programming") == 6
    assert count_vowels("Hello World") == 3

print(count_vowels("Hello World")) # returns 3
print(test_count_vowels()) # returns None