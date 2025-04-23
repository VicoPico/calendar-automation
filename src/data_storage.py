# In-memory storage for events
stored_events = []


def save_event(event_name, event_place, attendees):
    """
    Saves an event to the in-memory storage.
    """
    event = {
        "name": event_name,
        "place": event_place,
        "attendees": attendees,
    }
    stored_events.append(event)


def check_duplicate(event_name, event_place, attendees):
    """
    Checks if an event with the same details already exists in storage.
    """
    for event in stored_events:
        if (
            event["name"] == event_name
            and event["place"] == event_place
            and set(event["attendees"]) == set(attendees)
        ):
            return True
    return False
