N = int(input("How many numbers: "))
Array = []
NegativeElements = []
NonPair = []

for i in range(N):
    element = int(input("Element " + str(i) + ": "))
    Array.append(element)

print("Min element: " + str(min((Array))))

for element in Array:
    if element < 0:
        NegativeElements.append(element)
    elif element % 2 != 0:
        NonPair.append(element)
print("Negative elements: " + str(NegativeElements))

sumNonPair = sum(NonPair)
countNonPair = len(NonPair)
if countNonPair != 0:
    average = sumNonPair/countNonPair
    print("Average: " + str(average))
else:
    print("NonPair arr is empty!")