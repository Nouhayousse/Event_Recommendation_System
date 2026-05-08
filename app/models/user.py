from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    field_of_study = Column(String)

    career_interest = Column(String)

    education_level = Column(String)

    interests = Column(String)

    interactions = relationship(
        "Interaction",
        back_populates="user"
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="user"
    )