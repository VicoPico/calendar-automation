import uuid
from datetime import datetime, timezone


def format_event_data(
    event_name, event_place, attendees, start_date_time, end_date_time
):
    """
    Formats event data into the iCalendar (.ics) format.
    """
    # Generate a unique identifier for the event
    uid = f"{uuid.uuid4()}@example.com"

    # Get the current timestamp in UTC for DTSTAMP
    dtstamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # Format start and end times to the correct iCalendar format
    dtstart = start_date_time.replace("-", "").replace(":", "").replace(" ", "T") + "00"
    dtend = end_date_time.replace("-", "").replace(":", "").replace(" ", "T") + "00"

    formatted_event = (
        "BEGIN:VEVENT\n"
        f"UID:{uid}\n"
        f"DTSTAMP:{dtstamp}\n"
        f"SUMMARY:{event_name}\n"
        f"LOCATION:{event_place}\n"
        f"DESCRIPTION:Attendees: {', '.join(attendees)}\n"
        f"DTSTART:{dtstart}\n"
        f"DTEND:{dtend}\n"
        "END:VEVENT\n"
    )
    return formatted_event


def generate_ics(
    event_name,
    event_place,
    attendees,
    start_date_time,
    end_date_time,
    filename="calendar.ics",
):
    """
    Generates or appends an event to a .ics calendar file.
    """
    event_data = format_event_data(
        event_name, event_place, attendees, start_date_time, end_date_time
    )

    # Write or append the event to the .ics file
    with open(filename, "a") as file:
        # If the file is empty, write the calendar header
        if file.tell() == 0:
            file.write("BEGIN:VCALENDAR\n")
            file.write("VERSION:2.0\n")
            file.write("PRODID:-//YourAppName//Calendar Automation App//EN\n")

        file.write(event_data)

        # Ensure the calendar ends properly
        file.write("END:VCALENDAR\n")
