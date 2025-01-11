from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Date,
    Text,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"

    CompanyID = Column(Integer, primary_key=True, autoincrement=True)
    CompanyName = Column(String, nullable=False)
    CompanyRegistrationNumber = Column(String, nullable=False, unique=True)
    CompanyOwnerName = Column(String, nullable=False)
    OwnerEmail = Column(String, nullable=False, unique=True)
    OwnerPhone = Column(String(15), nullable=False, unique=True)
    CompanyAddress = Column(Text, nullable=False)
    CompanyAddress2 = Column(Text, nullable=True)
    CompanyAddress3 = Column(Text, nullable=True)

    brand_ambassadors = relationship("BrandAmbassador", back_populates="company")


class BrandAmbassador(Base):
    __tablename__ = "brand_ambassador"

    BrandAmbassadorID = Column(Integer, primary_key=True, autoincrement=True)
    CompanyID = Column(Integer, ForeignKey("company.CompanyID"), nullable=False)
    BAFirstName = Column(String, nullable=False)
    BALastName = Column(String, nullable=False)
    RegistrationNo = Column(String, nullable=False, unique=True)
    BAEmail = Column(String, nullable=False, unique=True)
    BAPhone = Column(String(15), nullable=False, unique=True)
    BAPassword = Column(String, nullable=False)

    company = relationship("Company", back_populates="brand_ambassadors")
    sessions = relationship("Session", back_populates="brand_ambassador")


class Session(Base):
    __tablename__ = "session"

    SessionID = Column(Integer, primary_key=True, autoincrement=True)
    BrandAmbassadorID = Column(Integer, ForeignKey("brand_ambassador.BrandAmbassadorID"), nullable=False)
    SessionLocation = Column(String, nullable=False)
    SessionDate = Column(Date, nullable=False)
    SessionStart = Column(DateTime, nullable=False)
    SessionEnd = Column(DateTime, nullable=False)
    ApproachedValue = Column(Integer, nullable=False)
    EngagedValue = Column(Integer, nullable=False)
    PitchedValue = Column(Integer, nullable=False)
    ClosedValue = Column(Integer, nullable=False)
    OnboardedValue = Column(Integer, nullable=False)

    brand_ambassador = relationship("BrandAmbassador", back_populates="sessions")
