import time

def countdown_timer():
    # Get user input for countdown time in seconds
    seconds = int(input("Enter the time in seconds for countdown: "))

    # Countdown loop
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        timeformat = '{:02d}:{:02d}'.format(mins, secs)  # Format as MM:SS
        print(timeformat, end='\r')  # Print on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease the time by 1 second

    print("🚨 Time's up!")

# Start the countdown timer
countdown_timer()
