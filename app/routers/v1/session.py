from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database

router = APIRouter()


@router.post("/sessions/", response_model=schemas.Session)
def create_session(session: schemas.SessionCreate, db: Session = Depends(database.get_db)):
    return crud.create_session(db, session)

@router.get("/sessions/{session_id}", response_model=schemas.Session)
def get_session(session_id: int, db: Session = Depends(database.get_db)):
    session = crud.get_session(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.get("/sessions/brand_ambassador/{brand_ambassador_id}", response_model=list[schemas.Session])
def get_sessions(brand_ambassador_id: int, db: Session = Depends(database.get_db)):
    return crud.get_sessions_by_brand_ambassador(db, brand_ambassador_id)

@router.put("/sessions/{session_id}", response_model=schemas.Session)
def update_session(session_id: int, session: schemas.SessionCreate, db: Session = Depends(database.get_db)):
    updated_session = crud.update_session(db, session_id, session)
    if not updated_session:
        raise HTTPException(status_code=404, detail="Session not found")
    return updated_session

@router.delete("/sessions/{session_id}", response_model=schemas.Session)
def delete_session(session_id: int, db: Session = Depends(database.get_db)):
    deleted_session = crud.delete_session(db, session_id)
    if not deleted_session:
        raise HTTPException(status_code=404, detail="Session not found")
    return deleted_session
