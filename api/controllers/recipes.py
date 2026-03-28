from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, recipe):
    db_recipes = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount = recipe.amount
    )

    db.add(db_recipes)
    db.commit()
    db.refresh(db_recipes)
    return db_recipes

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id, recipes):
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    update_data = recipes.model_dump(exclude_unset=True)
    db_recipes.update(update_data, synchronize_session=False)
    db.commit()
    db_recipes.first()
    return db_recipes

def delete(db: Session, recipe_id):
    db_recipes = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipes.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



