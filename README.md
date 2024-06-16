# Metronome Sandbox
Metronome Sandbox is a Python project designed to interact with the Metronome API for testing and generating events. This project provides scripts to send various types of events to Metronome and includes utilities for generating random event data.

## Prerequisites
Ensure you have Python 3.11.8 installed on your system. You can check your Python version with the following command:

```bash
python --version
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/metronome-sandbox.git
cd metronome-sandbox
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root by copying the example.env file. Update the .env file with your specific configuration values.
```bash
cp example.env .env
```
    
## Usage
The `metronome_scripts.py` script provides various functions for testing and generating events in the Metronome system. Here are the available commands:

Generate a heartbeat event:
```python scripts/metronome_scripts.py test_heartbeat_event```

Generate an API call event:
Copypython scripts/metronome_scripts.py test_api_call_event

Generate multiple random events:
Copypython scripts/metronome_scripts.py generate_multiple_random_events

Test multiple events:
Copypython scripts/metronome_scripts.py test_multiple_events


File Structure

scripts/metronome_scripts.py: The main script file containing various functions for testing and generating events.
api/networking/metronome_networking_controller.py: The networking controller module for handling network-related operations.
api/logic_handlers/metronome_logic_handler.py: The logic handler module for processing and sending events.
api/utils/event_utils.py: Utility functions for generating random event data.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License.

Feel free to customize and expand upon this README file based on your specific project requirements and best practices.