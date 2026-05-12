from datetime import datetime
import pytz
from urllib.parse import urlparse

from app.core.logger import logger



class MeetupNormalizer:

    def normalize_event(self, raw_event):

        raw_date = raw_event.get("date")

        cleaned_date = raw_date.split("[")[0]

        parsed_date = datetime.fromisoformat(cleaned_date)
        #morocco_tz = pytz.timezone("Africa/Casablanca")
        start_date = parsed_date.astimezone(pytz.UTC)

        logger.info(
            f"Normalized date: {start_date}"
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
        raw_url = raw_event.get("url")
        parsed_url = urlparse(raw_url)
        clean_url=(
            f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        )

        normalized_event = {

            "title": raw_event.get("title"),

            "source": "meetup",

            "source_url": clean_url,

            "start_date": start_date,

            "is_online": raw_event.get("is_online"),

            "format": event_format,

            "location": location,

            "tags": raw_event.get("category"),

            "image_url": raw_event.get("image_url")
        }

        return normalized_event