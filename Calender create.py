from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


request_body = {
    'summary': 'DailyTask',  # The name of the calendar
    'timeZone': 'Asia/Kolkata'  # The time zone of the calendar
}

response = service.calendars().insert(body=request_body).execute()

print("Calendar created successfully:")
print(response)
