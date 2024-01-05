squares = []

for value in range(1, 21):
    squares.append(value ** 2)

print(squares)
print(f"Minimum: {min(squares)}\nMaximum: {max(squares)}\nSum: {sum(squares)}")