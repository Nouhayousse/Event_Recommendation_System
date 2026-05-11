from datetime import datetime


class MeetupNormalizer:

    def normalize_event(self, raw_event):

        raw_date = raw_event.get("date")

        cleaned_date = raw_date.split("[")[0]

        start_date = datetime.fromisoformat(
            cleaned_date
        )

        event_format = (
            "online"
            if raw_event.get("is_online")
            else "offline"
        )

        location = (
            "Online"
            if raw_event.get("is_online")
            else "Offline"
        )

        normalized_event = {

            "title": raw_event.get("title"),

            "source": "meetup",

            "source_url": raw_event.get("url"),

            "start_date": start_date,

            "is_online": raw_event.get("is_online"),

            "format": event_format,

            "location": location,

            "tags": raw_event.get("category"),

            "image_url": raw_event.get("image_url")
        }

        return normalized_event