def format_phone_number(number):
    if number == "":  
        return ""  # Base case: return an empty string if there's nothing left to process
    
    if number[0].isdigit():  
        # Keep the first character (a digit) and recurse on the rest
        return number[0] + format_phone_number(number[1:])
    else:
        # Skip the first character (non-digit) and recurse on the rest
        return format_phone_number(number[1:])

# Testing the result
print(format_phone_number("(123) 456-7890"))    # → "1234567890"
print(format_phone_number("  +1-800-555-0199  "))  # → "18005550199"
print(format_phone_number("987.654.3210"))     # → "9876543210"