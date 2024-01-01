with open('pi_million_digits.txt') as million_pi:
    all_lines = million_pi.readlines()

pi_string = ''
for line in all_lines:
    pi_string += line.strip()

birthday = '030790'

if birthday in pi_string:
    print("Yes - it's in pi.")
else:
    print("No - it's not in pi.")
