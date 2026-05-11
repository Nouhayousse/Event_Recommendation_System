from apscheduler.schedulers.blocking import BlockingScheduler

from app.connectors.meetup.connector import MeetupConnector
from app.connectors.eventbrite.connector import EventbriteConnector

from app.services.normalizer.MeetupNormalizer import MeetupNormalizer
from app.services.normalizer.event_normalizer import normalize_event

from app.mappers.meetup_mapper import MeetupMapper
from app.mappers.eventbrite_mapper import map_eventbrite_event

from app.services.seminar_service import save_multiple_seminars
from app.services.seminar_service import mark_expired_seminars

from app.database.database import SessionLocal




 

def run_eventbrite_pipeline():
    print("Running Eventbrite pipeline...")
    connector = EventbriteConnector()
    raw_events = connector.fetch_events()
    normalized_events = [normalize_event(event) for event in raw_events]
    seminars = [map_eventbrite_event(event) for event in normalized_events]
    db = SessionLocal()
    save_multiple_seminars(db, seminars)
    db.close()  
    print("Eventbrite pipeline completed.")



def run_meetup_pipeline():
    print("Running Meetup pipeline...")
    connector = MeetupConnector()
    normalizer = MeetupNormalizer()
    mapper = MeetupMapper()
    db = SessionLocal()
    raw_events = connector.fetch_events()
    normalized_events = [normalizer.normalize_event(event) for event in raw_events]
    seminars = [mapper.map_to_seminar(event) for event in normalized_events]
    save_multiple_seminars(db, seminars)
    db.close()  
    print("Meetup pipeline completed.")




def run_expiration_checker():
    print("Running expiration check...")
    db = SessionLocal()
    mark_expired_seminars(db)
    db.close()  
    print("Expiration check completed.")



scheduler=BlockingScheduler()

scheduler.add_job(run_eventbrite_pipeline, 'interval', hours=24)
scheduler.add_job(run_meetup_pipeline, 'interval', hours=24)
scheduler.add_job(run_expiration_checker, 'interval', hours=48)

if __name__ == "__main__":
    print("Starting seminar scheduler...")
    scheduler.start()