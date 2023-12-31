from random import choice


def generate_winning_numbers(possible_characters):
    winning_numbers = []
    for number in range(1, 5):
        winning_numbers.append(choice(possible_characters))
    return winning_numbers


def print_winning_numbers(winning_numbers):
    print(f"The winning number is:", end=' ')
    for number in winning_numbers:
        print(f"{number} ", end='')


winning_numbers = generate_winning_numbers(['k', 'l', 'e', 'z', 'h', 3, 5, 7, 1, 0, 2, 4, 6, 8, 9])
print_winning_numbers(winning_numbers)
