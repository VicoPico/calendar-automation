def format_event_data(event):
    formatted_event = f"BEGIN:VEVENT\n"
    formatted_event += f"SUMMARY:{event['name']}\n"
    formatted_event += f"LOCATION:{event['location']}\n"
    formatted_event += f"DESCRIPTION:{event['description']}\n"
    formatted_event += f"DTSTART:{event['start_time']}\n"
    formatted_event += f"DTEND:{event['end_time']}\n"
    formatted_event += f"END:VEVENT\n"
    return formatted_event


def write_to_ics(events, filename):
    with open(filename, "w") as file:
        file.write("BEGIN:VCALENDAR\n")
        file.write("VERSION:2.0\n")
        for event in events:
            file.write(format_event_data(event))
        file.write("END:VCALENDAR\n")
