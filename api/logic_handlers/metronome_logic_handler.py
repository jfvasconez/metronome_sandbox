from api.networking.metronome_networking_controller import MetronomeNetworkingController

class MetronomeLogicHandler:
    # Function to generate a single event
    @staticmethod
    def send_event(transaction_id, customer_id, event_type, timestamp, properties):
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
    @staticmethod
    def send_multiple_events(events):
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