from ics import Calendar
import requests, arrow

url = "https://calendar.google.com/calendar/ical/rneventteknik%40gmail.com/public/basic.ics"
c = Calendar(requests.get(url).text)

def cal_generator(calendar: Calendar, full_name: str, initals: str):
    my_events = Calendar()

    for e in list(calendar.timeline.start_after(arrow.now())):
        name = e.name
        
        # if not a gig but contains Name
        if "]" not in name:
            if full_name in name.lower():
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

        for name in names:
            if initals == name:
                my_events.events.add(e)
    
    return my_events


with open('Tessa.ics', 'w') as f:
    f.writelines(cal_generator(c, "tessa", "TY").serialize_iter())

with open('Daniel.ics', 'w') as f:
    f.writelines(cal_generator(c, "daniel", "DS").serialize_iter())

with open('Daniel.ics', 'r') as f:
    print(f.read())