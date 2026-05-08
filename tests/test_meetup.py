import sys
from pathlib import Path

# Ajouter le dossier parent au chemin
sys.path.append(str(Path(__file__).parent.parent))



from app.connectors.meetup.connector import MeetupConnector


connector = MeetupConnector()

connector.fetch_events()

