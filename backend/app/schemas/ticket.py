from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..models.ticket import Status

class TicketBase(BaseModel):
    subject: str
    description: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    status: Optional[Status]

class TicketInDBBase(TicketBase):
    id: int
    user_id: int
    status: Status
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Ticket(TicketInDBBase):
    pass
