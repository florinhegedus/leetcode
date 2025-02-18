import re


def valid_palindrome(s):
    s = re.sub("[^0-9a-zA-Z]", "", s)  # s = ''.join(c.lower() for c in s if c.isalnum())
    s = s.lower()
    print(s)

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


if __name__ == '__main__':
    print(valid_palindrome("Ana are mere, si pere!"))
    print(valid_palindrome("abccba"))
    print(valid_palindrome(" "))
