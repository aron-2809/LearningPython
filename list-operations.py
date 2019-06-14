numbers = [5, 2, 1, 7, 4, 7]
# print(numbers.sort())
# numbers.reverse()
# print(numbers)

result = []
for elem in numbers:
    if elem not in result:
        result.append(elem)

print(result)
