from collections import Counter


def check_palindrome(s):
    counter = Counter(s)
    odd_count = 0
    odd_char = ""
    palindrome = []

    for char, count in counter.items():
        if count % 2 == 1:
            odd_count += 1
            odd_char = char
        palindrome.append(char * (count // 2))

    if odd_count > 1:
        return "I'm Sorry Hansoo"
    else:
        palindrome.sort()
        return "".join(palindrome) + odd_char + "".join(palindrome[::-1])


print(check_palindrome(input()))
