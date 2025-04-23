from data_storage import stored_events
from typing import List, Dict


def suggest_events(event_name: str) -> List[str]:
    """
    Suggests similar events based on the event name.
    """
    suggestions = []
    for event in stored_events:
        if event_name.lower() in event["name"].lower():
            suggestions.append(event["name"])
    return suggestions


class EventSuggestion:
    def __init__(self, events: List[Dict]):
        self.events = events

    def get_unique_attendees(self) -> List[str]:
        attendees = set()
        for event in self.events:
            attendees.update(event["attendees"])
        return list(attendees)
