from Google import Create_Service
from datetime import datetime, timedelta

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_request_body = {
    'summary': 'Project Track',
    'timeZone': 'Asia/Kolkata'
}
calendar_response = service.calendars().insert(body=calendar_request_body).execute()
calendar_id = calendar_response['id']

start_time = datetime(2024, 6, 15, 13, 30, 0)  # (yyyy, mm, dd, hr, min, sec)
end_time = start_time + timedelta(hours=2)
time_zone = 'Asia/Kolkata'

# Create the event request body
event_request_body = {
    'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': time_zone,
    },
    'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': time_zone
    },
    'summary': 'MLProj Meet',
    'description': 'Discussion of the final year project',
    'colorId': 5,
    'status': 'confirmed',
    'transparency': 'opaque',
    'visibility': 'private',
    'location': 'Thane, Viviana',
    'attendees': [
        {
            'displayName': 'Tom',
            'comment': 'cool guy',
            'email': 'tp@example.com',
            'optional': False,  # Indicates if this attendee is optional
            'organizer': True,
            'responseStatus': 'accepted'
        }
    ]
}

max_attendees = 5
send_notifications = True
send_updates = 'none'

event_response = service.events().insert(
    calendarId=calendar_id,
    maxAttendees=max_attendees,
    sendNotifications=send_notifications,
    sendUpdates=send_updates,
    body=event_request_body,
).execute()

print("Event created successfully:")
print(event_response)
