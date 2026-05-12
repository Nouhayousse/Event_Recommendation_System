from app.models.seminar import Seminar


class EventbriteMapper:

    def map_to_seminar(
        self,
        event: dict
    ) -> Seminar:

        location_type = event.get(
            "location_type"
        )

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

            is_expired=False,

            start_date=event.get("date"),

            end_date=event.get("end_date"),

            tags=event.get("category"),

            image_url=event.get("image_url")
        )

        return seminar