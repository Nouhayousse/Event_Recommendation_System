from sqlalchemy.orm import Session

from app.models.seminar import Seminar


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