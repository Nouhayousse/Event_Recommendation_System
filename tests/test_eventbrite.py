import sys
from pathlib import Path

# Ajouter le dossier parent au chemin
sys.path.append(str(Path(__file__).parent.parent))



from app.connectors.eventbrite.connector import EventbriteConnector

from app.services.normalizer.event_normalizer import (
    normalize_event
)

from app.mappers.eventbrite_mapper import map_eventbrite_event
from app.services.seminar_service import save_seminar
from app.services.seminar_service import save_multiple_seminars

from app.database.database import SessionLocal
db = SessionLocal()

connector = EventbriteConnector()

events = connector.fetch_events()
mapped_seminars = []
for event in events:
    normalized_event = normalize_event(event)
    seminar = map_eventbrite_event(normalized_event)
    
    mapped_seminars.append(seminar)

save_multiple_seminars(db, mapped_seminars)
    