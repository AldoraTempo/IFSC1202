def is_special_number(n):
    """Check if a number is a special (Armstrong) number."""
    original_number = n
    num_digits = 0
    sum_of_powers = 0
    
    temp_number = n
    while temp_number > 0:
        num_digits += 1
        temp_number //= 10  

    temp_number = original_number
    while temp_number > 0:
        digit = temp_number % 10 
        sum_of_powers += digit ** num_digits  
        temp_number //= 10  

    return sum_of_powers == original_number

def special_numbers_in_range(start, end):
    """Display a list of special numbers in the specified range."""
    return [num for num in range(start, end + 1) if is_special_number(num)]

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

special_numbers = special_numbers_in_range(start_range, end_range)
print(f"Special numbers between {start_range} and {end_range}: {special_numbers}")
