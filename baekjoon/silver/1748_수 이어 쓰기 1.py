n = int(input())


def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def count_numbers(num_digits):
    count = 0
    for i in range(1, num_digits):
        count += i * (9 * 10**(i-1))
    return count


num_digits = count_digits(n)
result = count_numbers(num_digits) + \
    (n - 10**(num_digits-1) + 1) * num_digits
print(result)
