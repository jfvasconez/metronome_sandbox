# scripts/event_utils.py
import random
import uuid
from datetime import datetime

# Generate a random UUID
def generate_uuid():
    return str(uuid.uuid4())

# Generate a random timestamp between two dates
def generate_random_timestamp(start_date, end_date):
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())
    random_timestamp = random.randint(start_timestamp, end_timestamp)
    return datetime.utcfromtimestamp(random_timestamp).isoformat() + "Z"

# Generate a random number of tokens between 50 and 1500
def generate_random_tokens():
    return random.randint(50, 1500)

# Choose a random region from the list
def generate_random_region():
    regions = ["USA", "Europe", "South America", "Africa", "Australia", "China", "Japan"]
    return random.choice(regions)

# Choose a random model name from the list
def generate_random_model_name():
    model_names = ["gpt-4o-2024-05-13", "gpt-4-turbo", "gpt-3.5-turbo-0125"]
    return random.choice(model_names)

# Choose a random usage tier from the list
def generate_random_usage_tier():
    usage_tiers = ["free", "premium", "custom", "basic"]
    return random.choice(usage_tiers)

# Choose a random boolean value for batch
def generate_random_batch():
    return random.choice([True, False])

# Choose a random model type from the list
def generate_random_model_type():
    model_types = ["text_generation", "image", "audio"]
    return random.choice(model_types)

# Generate a random number of CPU seconds between 10 and 500
def generate_random_cpu_seconds():
    return random.randint(10, 500)

# Generate a random cluster ID between 0 and 100
def generate_random_cluster_id():
    return random.randint(0, 100)
