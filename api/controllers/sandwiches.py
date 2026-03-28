from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, sandwich):
    db_sandwiches = models.Sandwich(
        sandwich_name = sandwich.sandwich_name,
        price = sandwich.price
    )
    db.add(db_sandwiches)
    db.commit()
    db.refresh(db_sandwiches)
    return db_sandwiches

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwiches_id, sandwiches):
    db_sandwiches = db.query(models.Sandwich).filter(models.Sandwich.id == sandwiches_id)

    update_data = sandwiches.model_dump(exclude_unset=True)

    db_sandwiches.update(update_data, synchronize_session=False)
    db.commit()
    db_sandwiches.first()
    return db_sandwiches.first()

def delete(db: Session, sandwich_id):
    db_sandwiches = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    db_sandwiches.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


