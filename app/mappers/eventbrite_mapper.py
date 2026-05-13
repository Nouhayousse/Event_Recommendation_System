from app.models.seminar import Seminar

from datetime import datetime
from zoneinfo import ZoneInfo




class EventbriteMapper:

    #now = datetime.now( ZoneInfo("Africa/Casablanca") )

    def map_to_seminar(
        self,
        event: dict
    ) -> Seminar:

        location_type = event.get(
            "location_type"
        )

        #start_date = event.get("date")
        #now=datetime.now( ZoneInfo("Africa/Casablanca") )
        #is_expired = False

        seminar = Seminar(

            title=event.get("title"),

            source="eventbrite",

            source_url=event.get("url"),

            location=(
                "Online"
                if location_type == "online"
                else "Offline"
            ),

            format=location_type,

            is_online=(
                location_type == "online"
            ),

            start_date=event.get("date"),
            is_expired=False,

            end_date=event.get("end_date"),

            tags=event.get("category"),

            image_url=event.get("image_url")
        )

        return seminar