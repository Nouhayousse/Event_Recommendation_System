from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Boolean,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base

class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    seminar_id = Column(
        Integer,
        ForeignKey("seminars.id")
    )

    clicked = Column(Boolean, default=False)

    saved = Column(Boolean, default=False)

    registered = Column(Boolean, default=False)

    attended = Column(Boolean, default=False)

    interaction_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="interactions"
    )

    seminar = relationship(
        "Seminar",
        back_populates="interactions"
    )