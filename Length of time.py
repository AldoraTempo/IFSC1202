def convert_time(total_seconds: float):
    total_seconds = int(total_seconds)
    
    years = total_seconds // 31536000
    remainder = total_seconds % 31536000

    weeks = remainder // 604800
    remainder = remainder % 604800

    days = remainder // 86400
    remainder = remainder % 86400

    hours = remainder // 3600
    remainder = remainder % 3600

    minutes = remainder // 60
    seconds = remainder % 60

    # Print results
    print(f"Years:   {years}")
    print(f"Weeks:   {weeks}")
    print(f"Days:    {days}")
    print(f"Hours:   {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")


# Example usage:
time_in_seconds = float(input("Enter time in seconds: "))
convert_time(time_in_seconds)
