from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Float,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base

class Recommendation(Base):

    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    seminar_id = Column(
        Integer,
        ForeignKey("seminars.id")
    )

    score = Column(Float)

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="recommendations"
    )

    seminar = relationship(
        "Seminar",
        back_populates="recommendations"
    )