# db/init_db.py

from sqlalchemy.orm import Session
from .session import SessionLocal
from .. import models

def init_db(db: Session):
    pass
    # Optional: Add code to create initial database records
    
    # Example to create an initial user, modify according to your model
    # demo_user = models.User(username="demo", email="demo@example.com", password_hash="hashedpassword")
    # db.add(demo_user)
    # db.commit()

def main():
    db = SessionLocal()
    init_db(db)

if __name__ == "__main__":
    main()
