# api/networking/metronome_networking_controller.py
from instances.metronome_instance import metronome_client

class MetronomeNetworkingController:
    @staticmethod
    def ingest_event(transaction_id, customer_id, event_type, timestamp, properties):
        url = "https://api.metronome.com/v1/ingest"
        payload = [
            {
                "transaction_id": transaction_id,
                "customer_id": customer_id,
                "event_type": event_type,
                "timestamp": timestamp,
                "properties": properties
            }
        ]
        response = metronome_client.session.post(url, json=payload)
        return response
    
    @staticmethod
    def ingest_multiple_events(events):
        url = "https://api.metronome.com/v1/ingest"
        response = metronome_client.session.post(url, json=events)
        return response