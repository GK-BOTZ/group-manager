from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from MahakRobot import DB_URI
from MahakRobot import LOGGER as log

# Adjust DB_URI if necessary
if DB_URI and DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)

# Base class for declarative models
BASE = declarative_base()

def start() -> scoped_session:
    if not DB_URI:
        log.error("[PostgreSQL] Database URI is not defined or is empty.")
        exit(1)

    try:
        # Create engine
        engine = create_engine(DB_URI, client_encoding="utf8")
        log.info("[PostgreSQL] Connecting to database...")

        # Bind metadata and create tables
        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)

        # Return a new scoped session
        return scoped_session(sessionmaker(bind=engine, autoflush=False))

    except exc.SQLAlchemyError as e:
        log.exception(f"[PostgreSQL] Database connection failed: {e}")
        exit(1)

# Initialize session
try:
    SESSION = start()
    log.info("[PostgreSQL] Connection successful, session started.")
except Exception as e:
    log.exception(f"[PostgreSQL] Unexpected error: {e}")
    exit(1)