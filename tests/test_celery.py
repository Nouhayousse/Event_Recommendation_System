from pathlib import Path
import sys

# Ajouter le dossier parent au chemin
sys.path.append(str(Path(__file__).parent.parent))

from app.tasks.meetup_tasks import scrape_meetup_task

scrape_meetup_task.delay()