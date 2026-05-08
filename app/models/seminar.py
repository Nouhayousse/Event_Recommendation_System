from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime
)

from sqlalchemy.orm import relationship

from app.database.base import Base

class Seminar(Base):

    __tablename__ = "seminars"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    source = Column(String)

    source_url = Column(String, unique=True)

    location = Column(String)

    format = Column(String)


    is_online = Column(Boolean, default=False)

    is_expired = Column(Boolean, default=False)

    start_date = Column(DateTime)

    end_date = Column(DateTime)

    tags = Column(String)

    interactions = relationship(
        "Interaction",
        back_populates="seminar"
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="seminar"
    )