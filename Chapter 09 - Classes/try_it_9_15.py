from random import choice


def generate_winning_numbers(possible_characters, pool_size):
    """Generates winning numbers by picking 'pool_size' number of random characters from a given list"""
    winning_numbers = []

    # Pick a random character from the list for number of times specified by pool_size. Return winning number list.
    for number in range(1, pool_size + 1):
        winning_numbers.append(choice(possible_characters))
    return winning_numbers


def check_if_winner(my_ticket, pool_size):
    """Take input list as user ticket. Go through while loop until my numbers match the numbers
     in the winning numbers pool."""

    winner = False
    iterations = 0

    while not winner:

        # Generate the winning numbers for a given pool_size.
        winning_numbers = generate_winning_numbers(['k', 'l', 'e', 'z', 'h', 3, 5, 7, 1, 0, 2, 4, 6, 8, 9], pool_size)
        matching_numbers = 0

        # Iterate through each number of my_ticket and check if it's in winning numbers. Count +1 if match.
        for number in my_ticket:
            if number in winning_numbers:
                matching_numbers += 1

        # Once number of matches equals pool size, we have a winner.
        if matching_numbers == pool_size:
            winner = True
            print(f"\n\nWinner Winner Chicken Dinner!")

        iterations += 1

        # Print out numbers even when losing.
        print(f"Current iteration: {iterations}")
        print(f"\t- Winning Numbers: {winning_numbers}")
        print(f"\t- My Ticket: {my_ticket}")
        print(f"\t- Matching Numbers: {matching_numbers}")


# Run the function
check_if_winner(['z', 'e', 'k', 8, 4, 0], 6)
