text = input("Введите строку:")
wowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"
result = ""
for char in text:
    if char not in wowels:
        result += char
print(result) 