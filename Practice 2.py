import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json

# Load credentials from token.json
creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# If credentials are expired, refresh them
if creds.expired and creds.refresh_token:
    creds.refresh(Request())

# Define the necessary headers
headers = {
    'Authorization': f'Bearer {creds.token}',
    'Accept': 'application/json',
}

# List upcoming events
response = requests.get('https://www.googleapis.com/calendar/v3/calendars/primary/events', headers=headers)
events = response.json().get('items', [])
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
