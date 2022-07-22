from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime
import requests

with open("id.txt","r") as f:
    id = f.readline()
lancsfeed="http://timetabling.lancaster.ac.uk/iCalendar/Personal.ics"

def main():
    cal = Calendar()
    
    ecal = cal.from_ical(requests.get(lancsfeed+"?ID="+id).text)    
    for component in ecal.walk():
        if component.name == "VEVENT":
            print(component.get("description"))
            print(component.get("organizer"))
            print(component.get("location"))
            print(component.decoded("dtstart"))
            print(component.decoded("dtend"))
            print()


if __name__ == "__main__":
    main()