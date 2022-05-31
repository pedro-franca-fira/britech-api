from app.Libs.db.database import Database

from app.Config import *

database = Database(DATABASE_DRIVER, DATABASE_SERVER, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD)

