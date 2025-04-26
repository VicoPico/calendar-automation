# Calendar Automation App

This project is a command-line application designed to automate the process of adding events to a calendar. Users can input event details, and the application will store this information, check for duplicates, and generate a calendar file in the .ics format.

## Features

- Add new events with details such as:
  - Event name
  - Event place
  - Attendees
  - Start and end date/time (used for `.ics` generation but not stored)
- Prevent duplicate events by checking existing data.
- Suggest alternative events based on previously stored data.
- Generate a `.ics` file containing multiple events.
- Isolated virtual environment for managing dependencies.

## Requirements

- Python 3.8 or higher
- Virtual environment (`venv`) for dependency management

## Project Structure

```
calendar-automation-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── calendar_utils.py     # Utility functions for .ics file generation
│   ├── data_storage.py       # Manages data storage and duplicate checking
│   └── event_suggestions.py   # Suggests alternative events
├── requirements.txt          # Project dependencies
├── .gitignore                # Files and directories to ignore in version control
├── README.md                 # Documentation for the project
└── venv/                     # Virtual environment directory
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd calendar-automation-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```powershell
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage Guidelines

To run the application, execute the following command in the terminal:

```bash
python src/main.py
```

Follow the prompts to input event details. The application will handle data storage and generate the calendar file accordingly.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
