from ics import Calendar, Event
import requests

url = "https://calendar.google.com/calendar/ical/rneventteknik%40gmail.com/public/basic.ics"
c = Calendar(requests.get(url).text)
c.events

e = list(c.timeline)[0]

print("Event '{}' started {}".format(e.name, e.begin.humanize()))