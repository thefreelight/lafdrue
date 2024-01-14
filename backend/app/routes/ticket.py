
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..schemas.ticket import TicketCreate, Ticket, TicketUpdate
from ..services.crud_ticket import create_ticket, get_ticket, get_tickets_for_user, update_ticket, delete_ticket
from ..database import SessionLocal
from ..dependencies.jwt_dependency import get_current_user,get_current_active_user
from ..models.user import User

router = APIRouter()

@router.post("/tickets/", response_model=Ticket)
def create_ticket_view(
    ticket_create: TicketCreate,
    db: Session = Depends(SessionLocal),
    current_user: User = Depends(get_current_active_user),
):
    return create_ticket(db=db, ticket_create=ticket_create, user_id=current_user.id)

@router.get("/tickets/{ticket_id}", response_model=Ticket)
def get_ticket_view(
    ticket_id: int,
    db: Session = Depends(SessionLocal),
    current_user: User = Depends(get_current_active_user),
):
    ticket = get_ticket(db, ticket_id)
    if ticket.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this ticket")
    return ticket

@router.get("/tickets/user/{user_id}", response_model=List[Ticket])
def get_tickets_for_user_view(
    user_id: int,
    db: Session = Depends(SessionLocal),
    current_user: User = Depends(get_current_active_user),
):
    if current_user.id != user_id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not authorized to access these tickets")
    return get_tickets_for_user(db, user_id)

@router.put("/tickets/{ticket_id}", response_model=Ticket)
def update_ticket_view(
    ticket_id: int,
    ticket_update: TicketUpdate,
    db: Session = Depends(SessionLocal),
    current_user: User = Depends(get_current_active_user),
):
    ticket = get_ticket(db, ticket_id)
    if ticket.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this ticket")
    return update_ticket(db, ticket_id, ticket_update)

@router.delete("/tickets/{ticket_id}")
def delete_ticket_view(
    ticket_id: int,
    db: Session = Depends(SessionLocal),
    current_user: User = Depends(get_current_active_user),
):
    ticket = get_ticket(db, ticket_id)
    if ticket.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this ticket")
    return delete_ticket(db, ticket_id)
