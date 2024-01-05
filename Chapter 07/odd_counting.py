# create variable and set value to 0
current_number = 0

# create while loop that functions while current # is less than 10,
# increment current number variable by 1, if current number is even, it
# is skipped. all odd numbers are printed.
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)