words = input("Введите текст: ")
splitWords = words.split()
print(splitWords)

last = -1
foundIt = False
symbol = 0
i = 0
while (foundIt == False):
    if splitWords[i][last].isalpha():
        symbol = str(splitWords[i][last])
        foundIt = True
    else:
        last -= 1

print(symbol)

while i < len(splitWords):
    splitWords[i] = splitWords[i].replace(symbol, "")
    i += 1

res = ' '.join(splitWords)
print(res)