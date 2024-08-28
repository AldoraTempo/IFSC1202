from datetime import datetime
time1 = input("")
time2 = input("")

time_format = "%H:%M:%S"
time1_obj = datetime.strptime(time1, time_format)
time2_obj = datetime.strptime(time2, time_format)

difference = time2_obj - time1_obj
seconds = difference.total_seconds()

print(seconds)