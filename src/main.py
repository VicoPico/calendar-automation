# main.py

import os
from calendar_utils import generate_ics
from data_storage import save_event, check_duplicate
from event_suggestions import suggest_events


def main():
    print("Welcome to the Calendar Automation App!")

    while True:
        event_name = input("Enter the name of the event: ")
        event_place = input("Enter the place of the event: ")
        attendees = input("Enter the names of attendees (comma-separated): ").split(",")

        # Ask for date and time (not stored)
        start_date_time = input(
            "Enter the start date and time of the event (YYYY-MM-DD HH:MM): "
        )
        end_date_time = input(
            "Enter the end date and time of the event (YYYY-MM-DD HH:MM): "
        )

        # Check for duplicates
        if check_duplicate(event_name, event_place, attendees):
            print("This event already exists. Please enter a different event.")
            continue

        # Save the event (excluding date and time)
        save_event(event_name, event_place, attendees)

        # Suggest alternatives
        suggestions = suggest_events(event_name)
        if suggestions:
            print("Here are some suggested alternatives based on previous events:")
            for suggestion in suggestions:
                print(f"- {suggestion}")

        # Generate the .ics file (include date and time for the event)
        generate_ics(event_name, event_place, attendees, start_date_time, end_date_time)

        another_event = (
            input("Do you want to add another event? (yes/no): ").strip().lower()
        )
        if another_event != "yes":
            break


if __name__ == "__main__":
    main()
