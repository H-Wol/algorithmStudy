n = int(input())
if n == 0:
    print('0')
    exit()

result = ''
while n != 0:
    remainder = n % -2
    n = (n // -2) + (1 if remainder < 0 else 0)
    result = str(abs(remainder)) + result

print(result)
