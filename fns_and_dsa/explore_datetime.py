import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    # formatted_date = current_date.strftime("%-d %b %Y %-I:%M%p").lower()
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime("%d %a %b %Y %-I:%M%p")}")


display_current_datetime()
calculate_future_date()