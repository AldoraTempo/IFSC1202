from datetime import datetime
time1 = input("")

hours, minutes, seconds = map(int, time1.split(':'))
total_seconds = hours * 3600 + minutes * 60 + seconds
print(total_seconds)