from app.database.database import engine
from app.database.base import Base

from app.models import *

Base.metadata.create_all(bind=engine)

print("Tables created successfully")