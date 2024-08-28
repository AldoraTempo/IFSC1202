from datetime import time
val1_str = input (time("", "", ""))
val2_str = input (time("", "", ""))
difference = val2_str - val1_str
print(difference.total_seconds()) # time difference in total seconds
print()