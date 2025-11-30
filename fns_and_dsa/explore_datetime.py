import datetime 
from datetime import date
def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date.strftime("Current date and time: %Y-%m-%d %H:%M:%S")
print(f"{display_current_datetime()}")
timedelta =int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(days):
    future_date = datetime.datetime.now() + datetime.timedelta(days=days)
    return future_date.strftime("Future date: %Y-%m-%d %H:%M:%S")
print(f'{calculate_future_date(timedelta)}')