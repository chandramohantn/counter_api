from sqlalchemy.orm import Session
from . import models, schemas


def create_brand_ambassador(db: Session, ambassador: schemas.BrandAmbassadorCreate):
    db_ambassador = models.BrandAmbassador(**ambassador.dict())
    db.add(db_ambassador)
    db.commit()
    db.refresh(db_ambassador)
    return db_ambassador

def get_brand_ambassador(db: Session, ambassador_id: int):
    return db.query(models.BrandAmbassador).filter(models.BrandAmbassador.BrandAmbassadorID == ambassador_id).first()

def get_brand_ambassadors_by_company(db: Session, company_id: int):
    return db.query(models.BrandAmbassador).filter(models.BrandAmbassador.CompanyID == company_id).all()

def update_brand_ambassador(db: Session, ambassador_id: int, ambassador: schemas.BrandAmbassadorCreate):
    db_ambassador = db.query(models.BrandAmbassador).filter(models.BrandAmbassador.BrandAmbassadorID == ambassador_id).first()
    if db_ambassador:
        for key, value in ambassador.dict().items():
            setattr(db_ambassador, key, value)
        db.commit()
        db.refresh(db_ambassador)
    return db_ambassador

def delete_brand_ambassador(db: Session, ambassador_id: int):
    db_ambassador = db.query(models.BrandAmbassador).filter(models.BrandAmbassador.BrandAmbassadorID == ambassador_id).first()
    if db_ambassador:
        db.delete(db_ambassador)
        db.commit()
    return db_ambassador
