s = input().strip()
result = []
is_tag = False
word = ""

for char in s:
    if char == "<":
        if word:
            result.append(word[::-1])
            word = ""
        is_tag = True
        result.append(char)
    elif char == ">":
        is_tag = False
        result.append(char)
    elif is_tag:
        result.append(char)
    else:
        if char == " ":
            if word:
                result.append(word[::-1])
                word = ""
            result.append(char)
        else:
            word += char

if word:
    result.append(word[::-1])

print("".join(result))
