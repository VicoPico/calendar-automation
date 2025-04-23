from typing import List, Dict

class EventSuggestion:
    def __init__(self, events: List[Dict]):
        self.events = events

    def suggest_events(self, keyword: str) -> List[Dict]:
        suggestions = []
        for event in self.events:
            if keyword.lower() in event['name'].lower() or keyword.lower() in event['place'].lower():
                suggestions.append(event)
        return suggestions

    def get_unique_attendees(self) -> List[str]:
        attendees = set()
        for event in self.events:
            attendees.update(event['attendees'])
        return list(attendees)