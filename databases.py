from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
import os
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Detection(Base):
    __tablename__ = "detections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    path_to_result = Column(Text)
    detection_time = Column(Text)
    defect_count = Column(Integer)
    create_datetime = Column(DateTime, default=datetime.datetime.utcnow)
