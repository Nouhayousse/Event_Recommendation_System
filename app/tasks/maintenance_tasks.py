
from requests import RequestException

from app.celery_app import celery_app

from app.database.database import SessionLocal

from app.services.seminar_service import (
    mark_expired_seminars
)


@celery_app.task(
        bind=True,
        autoretry_for=(RequestException,),
        retry_backoff=True,
        retry_jitter=True,
        retry_kwargs={'max_retries': 5}
)
def mark_expired_seminars_task(*args, **kwargs):

    print(
        "Running expired seminars task..."
    )

    db = SessionLocal()

    mark_expired_seminars(db)

    db.close()

    print(
        "Expired seminars task completed."
    )
