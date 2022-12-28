import sqlalchemy
from databases import Database

from kaiyuanshe_werobot.settings import settings


database = Database(settings.DATABASE_URL)


metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(255), nullable=False, unique=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column("is_superuser", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=sqlalchemy.func.now(), onupdate=sqlalchemy.func.now()),
    sqlalchemy.Column("deleted_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("is_deleted", sqlalchemy.Boolean, default=False),
    sqlalchemy.Column("email", sqlalchemy.String(255), nullable=False, unique=True),
    sqlalchemy.Column("full_name", sqlalchemy.String(255), nullable=True),
    sqlalchemy.Column("avatar", sqlalchemy.String(255), nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String(255), nullable=True),
)

engine = sqlalchemy.create_engine(
    settings.DATABASE_URL
)
metadata.create_all(engine)
