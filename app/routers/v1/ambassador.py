from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database

router = APIRouter()


@router.post("/brand_ambassadors/", response_model=schemas.BrandAmbassador)
def create_brand_ambassador(ambassador: schemas.BrandAmbassadorCreate, db: Session = Depends(database.get_db)):
    return crud.create_brand_ambassador(db, ambassador)

@router.get("/brand_ambassadors/{ambassador_id}", response_model=schemas.BrandAmbassador)
def get_brand_ambassador(ambassador_id: int, db: Session = Depends(database.get_db)):
    ambassador = crud.get_brand_ambassador(db, ambassador_id)
    if not ambassador:
        raise HTTPException(status_code=404, detail="Brand Ambassador not found")
    return ambassador

@router.get("/brand_ambassadors/company/{company_id}", response_model=list[schemas.BrandAmbassador])
def get_brand_ambassadors(company_id: int, db: Session = Depends(database.get_db)):
    return crud.get_brand_ambassadors_by_company(db, company_id)

@router.put("/brand_ambassadors/{ambassador_id}", response_model=schemas.BrandAmbassador)
def update_brand_ambassador(ambassador_id: int, ambassador: schemas.BrandAmbassadorCreate, db: Session = Depends(database.get_db)):
    updated_ambassador = crud.update_brand_ambassador(db, ambassador_id, ambassador)
    if not updated_ambassador:
        raise HTTPException(status_code=404, detail="Brand Ambassador not found")
    return updated_ambassador

@router.delete("/brand_ambassadors/{ambassador_id}", response_model=schemas.BrandAmbassador)
def delete_brand_ambassador(ambassador_id: int, db: Session = Depends(database.get_db)):
    deleted_ambassador = crud.delete_brand_ambassador(db, ambassador_id)
    if not deleted_ambassador:
        raise HTTPException(status_code=404, detail="Brand Ambassador not found")
    return deleted_ambassador
