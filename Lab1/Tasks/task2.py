n = int(input("Введіть кількість годин: "))

amoeba = 1

for i in range(n // 3):
    amoeba *= 2

print("Через", n, "годин буде", amoeba, "амеб")