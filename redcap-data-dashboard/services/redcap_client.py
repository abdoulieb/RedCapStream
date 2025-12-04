import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("REDCAP_API_URL")
API_TOKEN = os.getenv("REDCAP_API_TOKEN")

def fetch_redcap_data():
    """Fetch all records from REDCap."""
    payload = {
        'token': API_TOKEN,
        'content': 'record',
        'format': 'json',
        'type': 'flat'
    }

    response = requests.post(API_URL, data=payload)

    if response.status_code != 200:
        raise Exception(f"REDCap API error: {response.status_code} - {response.text}")

    df = pd.DataFrame(response.json())
    return df
