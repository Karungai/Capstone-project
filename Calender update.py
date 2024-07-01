from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

response = service.calendarList().list().execute()

calendar_items = response.get('items')

my_calendar = filter(lambda x: 'DailyTask' in x['summary'], calendar_items)
my_calendar = next(my_calendar)

my_calendar['summary'] = 'Daily Task'
my_calendar['description'] = 'Tasks that need to be done'

service.calendars().update(calendarId=my_calendar['id'], body=my_calendar).execute()

print("Calendar updated successfully:")
print(my_calendar)
