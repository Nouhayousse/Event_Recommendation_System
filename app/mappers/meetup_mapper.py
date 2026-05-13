import datetime
from zoneinfo import ZoneInfo

from app.core.logger import logger
from app.models.seminar import Seminar
from datetime import datetime


class MeetupMapper:

    def map_to_seminar(self, normalized_event):

        #start_date = normalized_event.get("start_date")
        #now = datetime.now( ZoneInfo("Africa/Casablanca") )
        #is_expired = (start_date < now if start_date else False)

        seminar = Seminar(

            title=normalized_event.get("title"),

            source=normalized_event.get("source"),

            source_url=normalized_event.get("source_url"),

            location=normalized_event.get("location"),

            format=normalized_event.get("format"),

            is_online=normalized_event.get("is_online"),

            start_date=normalized_event.get("start_date"),

            is_expired=False,

            tags=normalized_event.get("tags"),
            image_url=normalized_event.get("image_url")
        )
        logger.info(
          f"Mapped seminar date: {seminar.start_date}"
        )

        return seminar