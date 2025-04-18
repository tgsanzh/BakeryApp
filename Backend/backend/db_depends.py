from Backend.backend.db import session

async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
