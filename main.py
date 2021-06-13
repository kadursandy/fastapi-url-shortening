from fastapi import FastAPI, Depends
import models
import schemas
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from crud import get_stored_url, generate_short_url, get_all_short_urls
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/urlshortener")
def create_a_short_url(url_in: schemas.LongUrl, db: Session = Depends(get_db)):
    record = generate_short_url(db=db, url_in=url_in)
    return record


@app.get("/storedurl/{short_word}")
def get_long_url(short_word: str, db: Session = Depends(get_db)):
    record = get_stored_url(db=db, short_word=short_word)
    return record


@app.get("/urls", response_model=List[schemas.ResponseUrl])
def get_urls(db: Session = Depends(get_db)):
    return get_all_short_urls(db=db)
