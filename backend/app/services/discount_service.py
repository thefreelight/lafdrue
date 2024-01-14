from ..models.user import User

def apply_role_discount(user: User, total_amount: float) -> float:
    if user.role:
        return total_amount * (1 - user.role.discount / 100)
    return total_amount
