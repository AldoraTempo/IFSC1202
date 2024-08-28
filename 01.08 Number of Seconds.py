from datetime import datetime
time1 = input("")

time_format = "%H:%M:%S"
time1_obj = datetime.strptime(time1, time_format)
seconds = time1_obj.total_seconds()

print(seconds)
