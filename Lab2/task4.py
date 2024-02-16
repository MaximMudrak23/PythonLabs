def EuclideanAlgorithm(a, b):
    if b == 0:
        return a
    return EuclideanAlgorithm(b, a % b)

a = int(input("Число a: "))
b = int(input("Число b: "))

if a < 0 or b < 0:
    print("a чи b менше 0!")
    exit()

gcd = EuclideanAlgorithm(a, b)

print("НОД(", a, ",", b, "):", gcd)
