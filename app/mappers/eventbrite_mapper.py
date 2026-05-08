from app.models.seminar import Seminar


def map_eventbrite_event(event: dict) -> Seminar:

    seminar = Seminar(

        title=event.get("title"),

        source="eventbrite",

        source_url=event.get("url"),

        location=event.get("location"),

        format=event.get("location_type"),


        is_online=event.get("location_type") == "online",

        is_expired=False,

        start_date=event.get("date"),

        end_date=event.get("end_date"),

        tags=event.get("category")
    )

    return seminar