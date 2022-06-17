from .db_config_util import db_config

user = db_config["POSTGRES_USER"]
password = db_config["POSTGRES_PASSWORD"]
host = db_config["POSTGRES_HOST"]
port = db_config["POSTGRES_PORT"]
database = db_config["POSTGRES_DB"]


DATABASE_CONNECTION_URI = (
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
)
