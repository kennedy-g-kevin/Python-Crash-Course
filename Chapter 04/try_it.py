# numbers = []

# for number in range(1,1000001):
#     numbers.append(number)

# print(f"Sum: {sum(numbers)}\nMinimum: {min(numbers)}\nMaximum: {max(numbers)}")

# for number in range(1, 20, 2):
#     print(number)

# for number in range(3, 30, 3):
#     print(number)

# for number in range(1, 11):
#     numbers.append(number ** 3)

# print(numbers)

numbers = [number ** 3 for number in range(1, 11)]
print(numbers)