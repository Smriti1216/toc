def is_equal_a_and_b(input_string):
    current_state = 'q0'
    for char in input_string:
        if current_state == 'q0':
            if char == 'a':
                current_state = 'q2'
            elif char == 'b':
                current_state = 'q3'
            else:
                return False
        elif current_state == 'q2':
            if char == 'a':
                current_state = 'q2'
            elif char == 'b':
                current_state = 'q1'
            else:
                return False
        elif current_state == 'q3':
            if char == 'b':
                current_state = 'q3'
            elif char == 'a':
                current_state = 'q1'
            else:
                return False
        elif current_state == 'q1':
            if char != 'a' and char != 'b':
                return False
    return current_state == 'q1'

# Test cases
print(is_equal_a_and_b("ab"))      # True
print(is_equal_a_and_b("aabb"))    # True
print(is_equal_a_and_b("ababab"))  # True
print(is_equal_a_and_b("aaa"))     # False
print(is_equal_a_and_b("bbb"))     # False
print(is_equal_a_and_b("abc"))     # False
