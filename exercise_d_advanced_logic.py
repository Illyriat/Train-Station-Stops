# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = [i for i in numbers if i % 2 ==0]
print(even_numbers)


# 2. Print the difference between the largest and smallest value:
highest = max(numbers)
lowest = min(numbers)
difference = highest - lowest
print(difference)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
def has_2_next_to_2(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] == 2 and numbers[i+1] == 2:
            return True
    return False


# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
found_6 = False

for number in numbers:
    if number == 6:
        found_6 = True
    elif found_6 and number == 7:
        found_6 = False
    elif not found_6:
        total += number 

print(total)


# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

def unlucky_sum(numbers):
    total = 0
    skip = False

    for num in numbers:
        if num == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += num

    return total

print(unlucky_sum(numbers))
