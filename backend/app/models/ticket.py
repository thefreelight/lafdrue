from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from ..database import Base
import datetime
from enum import Enum as PyEnum

class Status(PyEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    subject = Column(String, index=True)
    description = Column(Text)
    status = Column(Enum(Status), default=Status.OPEN)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
