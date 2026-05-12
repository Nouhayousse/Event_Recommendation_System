
from app.celery_app import celery_app

from app.database.database import SessionLocal

from app.services.seminar_service import (
    mark_expired_seminars
)


@celery_app.task
def mark_expired_seminars_task():

    print(
        "Running expired seminars task..."
    )

    db = SessionLocal()

    mark_expired_seminars(db)

    db.close()

    print(
        "Expired seminars task completed."
    )
