from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
# load_dotenv(dotenv_path="D:/ML & NLP/Database/class 9/.env")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Debug print
print("User:", DB_USER)
print("Password:", DB_PASSWORD)
print("Host:", DB_HOST)
print("Port:", DB_PORT)
print("DB Name:", DB_NAME)

connetion_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connetion_string)
print(engine)

with engine.connect() as connection:
    print("database connected successful")

query = "SELECT * FROM book_table"
df = pd.read_sql(query, con=engine)
print(df)