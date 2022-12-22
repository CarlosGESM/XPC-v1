from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import settings



# Getting database url
database_url = settings.sqlalchemy_database_url

# Creating database engine
engine = create_engine(
    database_url, connect_args={
        "check_same_thread": False
    }
)

# Creating Session
SessionLocal1 = sessionmaker(
    autocommit=False, autoflush=False,
    bind=engine
)

#getting DB
Base = declarative_base()




#client = MongoClient(settings.mongodb_uri, settings.port)
#db = client['production']
