try:
    string = input("Enter a string: ").lower()
    
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    
    reverse_string = ""
    
    for char in string:
        reverse_string = char + reverse_string
    
    print("Reverse of the given string:", string, "is", reverse_string)
    
    if string == reverse_string:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")