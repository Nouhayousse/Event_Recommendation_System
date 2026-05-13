from sqlalchemy.orm import Session
from app.models.seminar import Seminar
from datetime import datetime
from zoneinfo import ZoneInfo
from app.core.logger import logger





def save_seminar(db: Session, seminar: Seminar):

    existing = db.query(Seminar).filter(
        Seminar.source_url == seminar.source_url
    ).first()

    if existing:
        new_date = seminar.start_date.replace(
            microsecond=0
        )
        existing_date = existing.start_date.replace(
            microsecond=0
        )


        #logger.info(f"Incoming date: {seminar.start_date}")
        #logger.info(f"Existing date: {existing.start_date}")

        #logger.info(
         #f"Incoming tzinfo: {seminar.start_date.tzinfo}"
        #)

        #logger.info(
         # f"Existing tzinfo: {existing.start_date.tzinfo}"
        #)

        #logger.info(
        # f"Incoming type: {type(seminar.start_date)}"
        #)

        #logger.info(
        # f"Existing type: {type(existing.start_date)}"
        #)


        #logger.info(
         # f"Incoming timestamp: "
         # f"{seminar.start_date.timestamp()}"
        #)

        #logger.info(
          #f"Existing timestamp: "
          #f"{existing.start_date.timestamp()}"
       #)
        if new_date != existing_date:
            #logger.info(
            #  f"Equality result: "
            #  f"{seminar.start_date == existing.start_date}"
            #)
            existing.start_date = seminar.start_date
            db.commit()
            return "updated"
            
        db.commit()
        return "exists"


    db.add(seminar)

    db.commit()


    return "inserted"


def save_multiple_seminars(
    db: Session,
    seminars: list[Seminar]
):

    inserted = 0
    updated = 0
    existed = 0

    for seminar in seminars:

        result = save_seminar(db, seminar)
        if result == "inserted":
            inserted += 1
        elif result == "updated":
            updated += 1
        elif result == "exists":
            existed += 1
    logger.info(f"Inserted {inserted} seminars, updated {updated} seminars, existed {existed} seminars.")





def mark_expired_seminars(db):

    now = datetime.now(ZoneInfo("Africa/Casablanca"))

    expired_seminars = db.query(Seminar).filter(
        Seminar.is_expired == False
    ).all()
    updated=0

    for seminar in expired_seminars:
       if(seminar.start_date < now):
           seminar.is_expired = True
           updated+=1
    db.commit()
    print(f"Marked {updated} seminars as expired.")