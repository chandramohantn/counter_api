from pydantic import BaseModel, EmailStr
from typing import Optional, List

class CompanyBase(BaseModel):
    CompanyName: str
    CompanyRegistrationNumber: str
    CompanyOwnerName: str
    OwnerEmail: EmailStr
    OwnerPhone: str
    CompanyAddress: str
    CompanyAddress2: Optional[str] = None
    CompanyAddress3: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    CompanyID: int

    class Config:
        orm_mode = True

class BrandAmbassadorBase(BaseModel):
    BAFirstName: str
    BALastName: str
    RegistrationNo: str
    BAEmail: EmailStr
    BAPhone: str

class BrandAmbassadorCreate(BrandAmbassadorBase):
    CompanyID: int
    BAPassword: str

class BrandAmbassador(BrandAmbassadorBase):
    BrandAmbassadorID: int

    class Config:
        orm_mode = True

class SessionBase(BaseModel):
    SessionLocation: str
    SessionDate: str
    SessionStart: str
    SessionEnd: str
    ApproachedValue: int
    EngagedValue: int
    PitchedValue: int
    ClosedValue: int
    OnboardedValue: int

class SessionCreate(SessionBase):
    BrandAmbassadorID: int

class Session(SessionBase):
    SessionID: int

    class Config:
        orm_mode = True
