from app.celery_app import celery_app

from app.connectors.eventbrite.connector import (
    EventbriteConnector
)

from app.services.normalizer.event_normalizer import (
    EventbriteNormalizer
)

from app.mappers.eventbrite_mapper import (
    EventbriteMapper
)

from app.services.seminar_service import (
    save_multiple_seminars
)

from app.database.database import (
    SessionLocal
)


@celery_app.task
def scrape_eventbrite_task():

    print("Running Eventbrite scraping task...")

    connector = EventbriteConnector()

    normalizer = EventbriteNormalizer()

    mapper = EventbriteMapper()

    db = SessionLocal()

    raw_events = connector.fetch_events()

    normalized_events = [

        normalizer.normalize_event(event)

        for event in raw_events
    ]

    seminars = [

        mapper.map_to_seminar(event)

        for event in normalized_events
    ]

    save_multiple_seminars(
        db,
        seminars
    )

    db.close()

    print(
        "Eventbrite scraping task completed."
    )