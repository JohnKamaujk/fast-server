from fastapi import FastAPI
from . import models
from .database import engine
from .routes import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
