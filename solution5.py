# Write code for algorithm 5 below
def is_a_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    return (str[0] == str[-1]) and is_a_palindrome(str[1:-1])

print(f"Is apple a palindrome? {is_a_palindrome('apple')}")
print(f"Is racecar a palindrome? {is_a_palindrome('racecar')}")