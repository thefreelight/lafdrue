
# schemas/admin_auth.py
from pydantic import BaseModel

# Schema for admin login
class AdminLogin(BaseModel):
    username: str
    password: str

# Schema for the token response
class AdminToken(BaseModel):
    access_token: str
    token_type: str
