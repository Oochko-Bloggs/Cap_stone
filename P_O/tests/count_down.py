import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')  # Overwrite the previous line
        time.sleep(1)
        time_sec -= 1

# Input time in seconds (e.g., 5 seconds)
t = int(input("Enter the time in seconds: "))
countdown(t)
print("Time's up!")
