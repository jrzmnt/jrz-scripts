"""
Adds a duration to a start time and returns the resulting time and day.

Parameters:
- start_time (str): A time in 12-hour format (e.g., '3:00 PM').
- duration (str): A duration in hours and minutes (e.g., '2:30').
- start_day (str, optional): A day of the week (e.g., 'Monday'). Case insensitive.

Returns:
- str: The new time in 12-hour format, optionally including the day of the week
       and the number of days later (e.g., '6:18 AM, Monday (20 days later)').

Example:
    add_time("8:16 PM", "466:02", "tuesday") 
    # Returns: '6:18 AM, Monday (20 days later)'
"""


def add_time(start_time, duration, start_day=None):
    # Split the start time into components
    time, period = start_time.split()
    hours, minutes = map(int, time.split(":"))
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Convert start time to 24-hour format
    if period == "PM":
        hours += 12

    # Add duration time
    total_minutes = hours * 60 + minutes + duration_hours * 60 + duration_minutes

    # Calculate new time and days passed
    new_hours = (total_minutes // 60) % 24
    new_minutes = total_minutes % 60
    days_passed = total_minutes // (24 * 60)

    # Convert back to 12-hour format
    new_period = "AM" if new_hours < 12 else "PM"
    if new_hours == 0:
        new_hours = 12
    elif new_hours > 12:
        new_hours -= 12

    # Format the new time
    new_time = f"{new_hours}:{new_minutes:02d} {new_period}"

    # Handle day of the week if provided
    if start_day:
        days_of_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        start_day_index = days_of_week.index(start_day.lower().capitalize())
        new_day_index = (start_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add days later information
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time


# Returns: '6:18 AM, Monday (20 days later)'
print(add_time("8:16 PM", "466:02", "tuesday"))
