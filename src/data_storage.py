from typing import List, Dict
import json
import os

DATA_FILE = 'events.json'

def load_events() -> List[Dict]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_events(events: List[Dict]) -> None:
    with open(DATA_FILE, 'w') as file:
        json.dump(events, file, indent=4)

def add_event(new_event: Dict) -> bool:
    events = load_events()
    if not any(event['name'] == new_event['name'] and event['date'] == new_event['date'] for event in events):
        events.append(new_event)
        save_events(events)
        return True
    return False

def event_exists(event_name: str, event_date: str) -> bool:
    events = load_events()
    return any(event['name'] == event_name and event['date'] == event_date for event in events)