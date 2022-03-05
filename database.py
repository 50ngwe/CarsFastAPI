from click import echo
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://techadmin@test-fast-api-db:Mustwork!!@test-fast-api-db.postgres.database.azure.com/item_db",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)

