seconds = int(input("Enter time in seconds: "))

# Convert step by step
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
weeks = days / 7
years = weeks / 52  # Approximate (not accounting for leap years)

# Display results
print(f"\nConversions:")
print(f"Seconds: {seconds}")
print(f"Minutes: {minutes:.2f}")
print(f"Hours:   {hours:.2f}")
print(f"Days:    {days:.2f}")
print(f"Weeks:   {weeks:.2f}")
print(f"Years:   {years:.2f}")
