from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def create_calendar_event(summary, description, start_datetime, end_datetime):
    creds = Credentials.from_authorized_user_info(info=user_info)
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'UTC',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')