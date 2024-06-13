# instances/metronome_instance.py
import os
from dotenv import load_dotenv
import requests

load_dotenv()
metronome_api_token = os.getenv('METRONOME_API_TOKEN')

class MetronomeClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_token}"
        })

metronome_client = MetronomeClient(api_token=metronome_api_token)