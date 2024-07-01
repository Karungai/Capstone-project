from Google import Create_Service
from pprint import pprint

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']  # Scope for Google Calendar API

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id = 'dgn1p9cn2rpltml651ffpbhkgs@group.calendar.google.com'
EventId = 'icd88r65bgm7rrd2iv30qcm2jk'

try:
    event = service.events().get(calendarId=calendar_id, eventId=EventId).execute()

    # Update the event's summary
    event['summary'] = 'Project Meet'

    # Save the updated event
    updated_event = service.events().update(calendarId=calendar_id, eventId=EventId, body=event).execute()

    # Print the updated event details
    pprint(updated_event)
except Exception as e:
    print(f"An error occurred: {e}")
