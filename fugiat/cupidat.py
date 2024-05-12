import time

# Get the current time in seconds since the epoch
current_time = time.time()

# Suspend the execution for 5 seconds
time.sleep(5)

# Get the current local time as a tuple
local_time = time.localtime()

# Convert the local time tuple to a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

# Print the formatted time
print(formatted_time)
