from app.core.logger import logger
from app.models.seminar import Seminar


class MeetupMapper:

    def map_to_seminar(self, normalized_event):

        seminar = Seminar(

            title=normalized_event.get("title"),

            source=normalized_event.get("source"),

            source_url=normalized_event.get("source_url"),

            location=normalized_event.get("location"),

            format=normalized_event.get("format"),

            is_online=normalized_event.get("is_online"),

            start_date=normalized_event.get("start_date"),

            tags=normalized_event.get("tags")
        )
        logger.info(
          f"Mapped seminar date: {seminar.start_date}"
        )

        return seminar