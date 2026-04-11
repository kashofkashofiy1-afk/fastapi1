from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from user import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial Assistant API")

@app.get("/")
def home():
    return {"message": "Xush kelibsix"}




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Mahsulot topilmadi")

    return {"message": "Mahsulot muvaffaqiyatli o'chirildi"}

@app.get("/products/", response_model=List[schemas.Product])
def read_products(
    search: str = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    products = crud.get_products(db, skip=skip, limit=limit, search=search)
    return products


