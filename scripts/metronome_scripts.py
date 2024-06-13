#scripts/metronome_scripts.py
import sys
import os
import json

# Adjust the path to include the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.networking.metronome_networking_controller import MetronomeNetworkingController

def generate_event(transaction_id, customer_id, event_type, timestamp, properties):
    try:
        response = MetronomeNetworkingController.ingest_event(
            transaction_id=transaction_id,
            customer_id=customer_id,
            event_type=event_type,
            timestamp=timestamp,
            properties=properties
        )
        if response:
            print(response)
            print(f"Response Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        else:
            print("No response received from the API.")
    except Exception as e:
        print(f"Error generating event: {str(e)}")

# python scripts/metronome_scripts.py test_event
def test_heartbeat_event():
    try:
        transaction_id = "2024-06-12T00:00:00Z_cluster42"
        customer_id = "juan@juan.com"
        event_type = "heartbeat"
        timestamp = "2024-06-12T00:00:00Z"
        properties = {
            "cluster_id": "42",
            "cpu_seconds": 60,
            "region": "Europe"
        }
        generate_event(transaction_id, customer_id, event_type, timestamp, properties)
    except Exception as e:
        print(f"Error in test_event: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "generate_event":
            transaction_id = input("Transaction ID: ")
            customer_id = input("Customer ID: ")
            event_type = input("Event Type: ")
            timestamp = input("Timestamp: ")
            properties = input("Properties (as a JSON string): ")
            try:
                properties = json.loads(properties)
            except json.JSONDecodeError:
                print("Invalid JSON for properties.")
                sys.exit(1)
            generate_event(transaction_id, customer_id, event_type, timestamp, properties)
        elif sys.argv[1] == "test_event":
            test_heartbeat_event()
        else:
            print("Invalid command. Usage:")
            print("python metronome_scripts.py generate_event")
            print("python metronome_scripts.py test_event")
    else:
        print("Usage:")
        print("python metronome_scripts.py generate_event")
        print("python metronome_scripts.py test_event")
