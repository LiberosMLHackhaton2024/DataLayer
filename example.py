from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://root:root@localhost:5432/HackML"
engine = create_engine(DATABASE_URL)

# Przykład użycia
with engine.connect() as connection:
    result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
    tables = result.fetchall()
    for table in tables:
        print(table)
