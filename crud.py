from sqlalchemy.orm import Session
import models
import schemas
import short_url


def generate_short_url(db: Session, url_in: schemas.LongUrl):
    add_url_rec = models.Url(long_url=url_in.long_url)
    db.add(add_url_rec)
    db.commit()
    rec_id = add_url_rec.id
    db.refresh(add_url_rec)

    short_word = short_url.encode_url(rec_id)
    record = db.query(models.Url).filter(models.Url.id == rec_id).first()
    # Change the browse url to bit.ly or tinyurl
    browse_url = "http://127.0.0.1:8000"
    record.short_url = f"{browse_url}/{short_word}"
    db.commit()
    db.refresh(record)
    return record


def get_stored_url(db: Session, short_word: str):
    long_url_id = short_url.decode_url(short_word.strip())
    record = db.query(models.Url).filter(models.Url.id == int(long_url_id)).first()
    return record


def get_all_short_urls(db: Session):
    recs = db.query(models.Url).all()
    return recs
