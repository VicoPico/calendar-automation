def format_event_data(
    event_name, event_place, attendees, start_date_time, end_date_time
):
    """
    Formats event data into the iCalendar (.ics) format.
    """
    formatted_event = "BEGIN:VEVENT\n"
    formatted_event += f"SUMMARY:{event_name}\n"
    formatted_event += f"LOCATION:{event_place}\n"
    formatted_event += f"DESCRIPTION:Attendees: {', '.join(attendees)}\n"
    formatted_event += (
        f"DTSTART:{start_date_time.replace('-', '').replace(':', '')}00\n"
    )
    formatted_event += f"DTEND:{end_date_time.replace('-', '').replace(':', '')}00\n"
    formatted_event += "END:VEVENT\n"
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

        file.write(event_data)
        file.write("END:VCALENDAR\n")
