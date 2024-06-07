def reverse_string(s):
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# Test reverse_string function
print("Reversed string:")
print(reverse_string("hello"))  # Output: "olleh"
