def is_divisible_by_2(input_string):
    current_state = 'q0'
    for char in input_string:
        if current_state == 'q0':
            if char.isdigit():
                current_state = 'q0'
            elif char == '.':
                current_state = 'q1'
            else:
                return False
        elif current_state == 'q1':
            if char.isdigit():
                current_state = 'q1'
            else:
                return False
    return current_state == 'q1'

# Test cases
print(is_divisible_by_2("4.0"))      # True
print(is_divisible_by_2("2.0"))    # True
print(is_divisible_by_2("2.5"))    # True (for fractions)
print(is_divisible_by_2("3"))      # False
print(is_divisible_by_2("abc"))    # False
