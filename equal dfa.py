def is_equal(input_string):
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

input_string =input("enter a equal no:")
if is_equal(input_string):
    print("string accepted")
else:
    print("string are not accepted")

