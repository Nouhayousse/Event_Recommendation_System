import sys
from pathlib import Path

# Ajouter le dossier parent au chemin
sys.path.append(str(Path(__file__).parent.parent))



from app.connectors.meetup.connector import MeetupConnector
from app.services.normalizer.MeetupNormalizer import MeetupNormalizer
from app.mappers.meetup_mapper import MeetupMapper
from app.database.database import SessionLocal
from app.services.seminar_service import save_multiple_seminars

connector = MeetupConnector()
normalizer = MeetupNormalizer()
mapper = MeetupMapper()
db = SessionLocal()
raw_events = connector.fetch_events()
normalized_events = [normalizer.normalize_event(event) for event in raw_events]
seminars = [mapper.map_to_seminar(event) for event in normalized_events]
save_multiple_seminars(db, seminars)
