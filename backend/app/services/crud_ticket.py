from sqlalchemy.orm import Session
from ..models.ticket import Ticket
from ..schemas.ticket import TicketCreate, TicketUpdate

def create_ticket(db: Session, ticket_create: TicketCreate, user_id: int) -> Ticket:
    ticket = Ticket(**ticket_create.dict(), user_id=user_id)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_ticket(db: Session, ticket_id: int) -> Ticket:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def get_tickets_for_user(db: Session, user_id: int):
    return db.query(Ticket).filter(Ticket.user_id == user_id).all()

def update_ticket(db: Session, ticket_id: int, ticket_update: TicketUpdate) -> Ticket:
    ticket =get_ticket(db, ticket_id)
    if ticket:
        for var, value in vars(ticket_update).items():
            setattr(ticket, var, value) if value else None
        db.commit()
        db.refresh(ticket)
        return ticket

def delete_ticket(db: Session, ticket_id: int):
        ticket = get_ticket(db, ticket_id)
        if ticket:
            db.delete(ticket)
            db.commit()
        return {"msg": "Ticket deleted successfully."}
