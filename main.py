from ics import Calendar
import requests, arrow

url = "https://calendar.google.com/calendar/ical/rneventteknik%40gmail.com/public/basic.ics"
c = Calendar(requests.get(url).text)

my_events = Calendar()

for e in list(c.timeline.start_after(arrow.now())):
    name = e.name
    
    # if not a gig but contains Name
    if "]" not in name:
        if "daniel" in name.lower():
            my_events.events.add(e)
        continue

    # if gig and contains name
    names = []
    for name in name.split("]")[0].strip().replace("[", "").split(","):
        name = name.strip()
        if len(name) == 2:
            names.append(name)
            continue
        for name in name.split( ):
            name = name.strip()
            if len(name) == 2:
                names.append(name)
                continue
    print(names)

    for name in names:
        if "DS" == name:
            my_events.events.add(e)


for e in list(my_events.timeline):
    print("Event '{}' started {}".format(e.name, e.begin.humanize()))