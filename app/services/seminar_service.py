from sqlalchemy.orm import Session
from app.models.seminar import Seminar
from datetime import datetime





def save_seminar(db: Session, seminar: Seminar):

    existing = db.query(Seminar).filter(
        Seminar.source_url == seminar.source_url
    ).first()

    if existing:
        return existing

    db.add(seminar)

    db.commit()

    db.refresh(seminar)

    return seminar


def save_multiple_seminars(
    db: Session,
    seminars: list[Seminar]
):

    saved = []

    for seminar in seminars:

        result = save_seminar(db, seminar)

        saved.append(result)

    return saved


def mark_expired_seminars(db):

    now = datetime.utcnow()

    seminars = db.query(Seminar).all()
    updated = 0
    for seminar in seminars:
        if seminar.start_date < now and not seminar.is_expired:
            seminar.is_expired = True
            updated += 1

    db.commit()
    print(f"Marked {updated} seminars as expired.")