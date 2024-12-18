def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    """Display a list of prime numbers in the specified range."""
    return [num for num in range(start, end + 1) if is_prime(num)]

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

primes = prime_numbers_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}: {primes}")
