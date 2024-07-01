from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id = 'rrtb7o5atcrpn86s1p78gdjn8c@group.calendar.google.com'

service.calendars().delete(calendarId=calendar_id).execute()

print(f"Calendar with ID {calendar_id} has been deleted.")
