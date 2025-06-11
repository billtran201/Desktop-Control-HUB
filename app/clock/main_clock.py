import datetime

def tell_time():
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format the time as a string in 12-hour clock format
    time_str = current_time.strftime("%I:%M:%S %p")
    print(f"The current time is: {time_str}")

    # Format the time as a string in 12-hour clock format
    hour_str = str(current_time.strftime("%I")).lstrip('0') or '0'
    minute_str = str(current_time.strftime("%M")).lstrip('0') or '0'
    period_str = current_time.strftime("%p")

    # Construct the final time string
    time_str = f"{hour_str} {minute_str} {period_str}"

    # Print or return the time
    
    return time_str

if __name__ == "__main__":
    tell_time()
