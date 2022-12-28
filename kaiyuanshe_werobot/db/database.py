
import databases
import sqlalchemy

from kaiyuanshe_werobot.settings import settings


database = databases.Database(settings.DATABASE_URL)


engine = sqlalchemy.create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

