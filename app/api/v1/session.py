from sqlalchemy.orm import Session
from . import models, schemas


def create_session(db: Session, session: schemas.SessionCreate):
    db_session = models.Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def get_session(db: Session, session_id: int):
    return db.query(models.Session).filter(models.Session.SessionID == session_id).first()

def get_sessions_by_brand_ambassador(db: Session, brand_ambassador_id: int):
    return db.query(models.Session).filter(models.Session.BrandAmbassadorID == brand_ambassador_id).all()

def update_session(db: Session, session_id: int, session: schemas.SessionCreate):
    db_session = db.query(models.Session).filter(models.Session.SessionID == session_id).first()
    if db_session:
        for key, value in session.dict().items():
            setattr(db_session, key, value)
        db.commit()
        db.refresh(db_session)
    return db_session

def delete_session(db: Session, session_id: int):
    db_session = db.query(models.Session).filter(models.Session.SessionID == session_id).first()
    if db_session:
        db.delete(db_session)
        db.commit()
    return db_session
