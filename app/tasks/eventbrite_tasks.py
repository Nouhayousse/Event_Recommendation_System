from requests import RequestException

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


@celery_app.task(
        bind=True,
        autoretry_for=(RequestException,),
        retry_backoff=True,
        retry_jitter=True,
        retry_kwargs={'max_retries': 5}
)
def scrape_eventbrite_task(*args, **kwargs):

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