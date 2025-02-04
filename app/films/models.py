from sqlalchemy import Column, Date, Float, Integer, String
from app.database import Base

class Films(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    release_date = Column(Date, index=True, nullable=False)
    rating = Column(Float, index=True)