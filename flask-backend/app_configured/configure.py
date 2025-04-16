from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
load_dotenv()  

db=SQLAlchemy()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
