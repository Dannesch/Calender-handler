from ics import Calendar
import requests, arrow

url = "https://calendar.google.com/calendar/ical/rneventteknik%40gmail.com/public/basic.ics"
c = Calendar(requests.get(url).text)

def cal_generator(calendar: Calendar, full_name: str, initals: str, add_internal: bool = True, add_misc: bool = True, add_pr: bool = False):
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

            if name.lower() == "internt" and add_internal:
                my_events.events.add(e)
                continue

            if ["fler", "flera", "alla"] in name.lower() and add_misc:
                my_events.events.add(e)
                continue

            if name.lower() == "pr" and add_pr:
                my_events.events.add(e)
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


with open('calendar/Tessa.ics', 'w') as f:
    f.writelines(cal_generator(c, "tessa", "TY", add_pr=True).serialize_iter())

with open('calendar/Daniel.ics', 'w') as f:
    f.writelines(cal_generator(c, "daniel", "DS").serialize_iter())