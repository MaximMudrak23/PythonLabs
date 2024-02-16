def calculate_a_n(x, n):
    if n == 0:
        return x
    else:
        prev_a = calculate_a_n(x, n-1)
        return prev_a + 1 / (prev_a + 2)

# Задачка з рекурсивним співвідношенням
x = float(input("Початкове значення a0: "))
n = int(input("К-сть ітерацій: "))
for i in range(n):
    a_i = calculate_a_n(x, i)
    print(f"a{i} = {a_i}")
