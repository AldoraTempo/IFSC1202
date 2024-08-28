import time
val1 = input("Enter time in HH:MM:SS\n")
val2 = input("Enter time in HH:MM:SS\n")
hour, min, sec = [int(i) for i in time.split(":")]
difference = val2 - val1
print(difference.total_seconds()) # time difference in total seconds
print()
