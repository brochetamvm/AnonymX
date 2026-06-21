from pydantic import BaseModel, Field
from typing import Optional

#Pydantic permite modelos aninhados (como Records dentro de Records no Delphi)
class UserAddress(BaseModel):
    city: str
    zipcode: str

class UserPII(BaseModel):
    id: int   
    # Exigimos que o nome seja texto e tenha pelo menos 2 caracteres
    name: str = Field(..., min_length=2)
    # Campo sensível (GDPR - E-mail)
    email: str
    # Campo sensível (GDPR - Telefone). Usamos Optional caso o usuário não tenha telefone
    phone: Optional[str] = None
    address: UserAddress