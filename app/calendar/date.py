# Calendar System
import datetime

def todayDate():
    # Get the current date
    current_date = datetime.date.today()

    # Format the date as a string with a placeholder for the calendar icon
    formatted_date = current_date.strftime("%A, %B %d, %Y")

    # Manually insert the calendar icon into the formatted date string
    formatted_date = f"📅 {formatted_date}"
    formatted_date = formatted_date.replace(" 0", " ")

    # Print the formatted date
    print(formatted_date)
    return str(formatted_date)