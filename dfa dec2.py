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
input_string =input("enter a decimal no:")
if is_divisible_by_2(input_string):
    print("string accepted")
else:
    print("string are not accepted")
