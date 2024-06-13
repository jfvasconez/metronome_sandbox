# scripts/metronome_scripts.py
import sys
import os
import json
import random
from datetime import datetime

# Adjust the path to include the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.networking.metronome_networking_controller import MetronomeNetworkingController
from api.utils.event_utils import (generate_uuid, 
                                   generate_random_timestamp, 
                                   generate_random_tokens, 
                                   generate_random_region, 
                                   generate_random_model_name, 
                                   generate_random_usage_tier, 
                                   generate_random_batch,
                                   generate_random_model_type, 
                                   generate_random_cpu_seconds, 
                                   generate_random_cluster_id
                                   )

# Function to generate a single event
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
            # print(f"Response Status Code: {response.status_code}")
            # print(f"Response: {response.json()}")
        else:
            print("No response received from the API.")
    except Exception as e:
        print(f"Error generating event: {str(e)}")

# Function to generate multiple events
def generate_multiple_events(events):
    try:
        response = MetronomeNetworkingController.ingest_multiple_events(events)
        if response:
            print(response)
            # print(f"Response Status Code: {response.status_code}")
            # print(f"Response: {response.json()}")
        else:
            print("No response received from the API.")
    except Exception as e:
        print(f"Error generating multiple events: {str(e)}")

# python scripts/metronome_scripts.py test_heartbeat_event
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

# python scripts/metronome_scripts.py test_api_call_event
def test_api_call_event():
    try:
        transaction_id = "2024-06-12T01:00:00Z_cluster42"
        customer_id = "juan@juan.com"
        event_type = "api_call"
        timestamp = "2024-06-12T01:00:00Z"
        properties = {
            "model_name": "gpt-3.5-turbo-0125",
            "model_type": "text_generation",
            "batch": "false",
            "input_tokens": 856,
            "output_tokens": 1024,
            "region": "USA",
            "usage_tier": "premium",
        }
        generate_event(transaction_id, customer_id, event_type, timestamp, properties)
    except Exception as e:
        print(f"Error in test_event: {str(e)}")

# python scripts/metronome_scripts.py test_multiple_random_events
def test_multiple_random_events():
    try:
        start_date = datetime(2024, 6, 7)
        end_date = datetime(2024, 6, 13)

        events = []
        for _ in range(100):  # Adjust the range for the number of events you want to generate
            event_type = random.choice(["heartbeat", "api_call"])
            properties = {}
            
            if event_type == "heartbeat":
                properties = {
                    "cluster_id": generate_random_cluster_id(),
                    "cpu_seconds": generate_random_cpu_seconds(),
                    "region": generate_random_region()
                }
            elif event_type == "api_call":
                properties = {
                    "model_name": generate_random_model_name(),
                    "model_type": generate_random_model_type(),
                    "batch": generate_random_batch(),
                    "input_tokens": generate_random_tokens(),
                    "output_tokens": generate_random_tokens(),
                    "region": generate_random_region(),
                    "usage_tier": generate_random_usage_tier()
                }
            
            event = {
                "transaction_id": generate_uuid(),
                "customer_id": "juan@juan.com",
                "event_type": event_type,
                "timestamp": generate_random_timestamp(start_date, end_date),
                "properties": properties
            }
            events.append(event)
        
        generate_multiple_events(events)
    except Exception as e:
        print(f"Error in test_multiple_events: {str(e)}")

# python scripts/metronome_scripts.py test_multiple_events
def test_multiple_events():
    try:
        events = [
            {
                "transaction_id": "multiple_events_heartbeat_2",
                "customer_id": "juan@juan.com",
                "event_type": "heartbeat",
                "timestamp": "2024-06-12T02:00:00Z",
                "properties": {
                    "cluster_id": "42",
                    "cpu_seconds": 60,
                    "region": "Europe"
                }
            },
            {
                "transaction_id": "multiple_events_api_call_2",
                "customer_id": "juan@juan.com",
                "event_type": "api_call",
                "timestamp": "2024-06-12T03:01:00Z",
                "properties": {
                    "model_name": "gpt-3.5-turbo-0125",
                    "model_type": "text_generation",
                    "batch": "false",
                    "input_tokens": 856,
                    "output_tokens": 1024,
                    "region": "USA",
                    "usage_tier": "premium",
                }
            }
        ]
        generate_multiple_events(events)
    except Exception as e:
        print(f"Error in test_multiple_events: {str(e)}")

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
        elif sys.argv[1] == "test_heartbeat_event":
            test_heartbeat_event()
        elif sys.argv[1] == "test_api_call_event":
            test_api_call_event()
        elif sys.argv[1] == "test_multiple_random_events":
            test_multiple_random_events()
        elif sys.argv[1] == "test_multiple_events":
            test_multiple_events()
        else:
            print("Invalid command. Usage:")
            print("python metronome_scripts.py generate_event")
            print("python metronome_scripts.py test_heartbeat_event")
            print("python metronome_scripts.py test_api_call_event")
            print("python metronome_scripts.py test_multiple_random_events")
            print("python metronome_scripts.py test_multiple_events")
    else:
        print("Usage:")
        print("python metronome_scripts.py generate_event")
        print("python metronome_scripts.py test_heartbeat_event")
        print("python metronome_scripts.py test_api_call_event")
        print("python metronome_scripts.py test_multiple_random_events")
        print("python metronome_scripts.py test_multiple_events")
