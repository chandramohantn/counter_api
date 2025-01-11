from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database

router = APIRouter()

@router.post("/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(database.get_db)):
    return crud.create_company(db, company)

@router.get("/companies/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(database.get_db)):
    company = crud.get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.get("/companies/", response_model=list[schemas.Company])
def read_companies(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_all_companies(db, skip=skip, limit=limit)

@router.put("/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyCreate, db: Session = Depends(database.get_db)):
    updated_company = crud.update_company(db, company_id, company)
    if not updated_company:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated_company

@router.delete("/companies/{company_id}", response_model=schemas.Company)
def delete_company(company_id: int, db: Session = Depends(database.get_db)):
    deleted_company = crud.delete_company(db, company_id)
    if not deleted_company:
        raise HTTPException(status_code=404, detail="Company not found")
    return deleted_company
