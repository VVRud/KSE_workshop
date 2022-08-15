import os
from sqlalchemy import create_engine, engine
from sqlalchemy import Column, Table, MetaData, String, Integer


class PostgresConn():
    def __init__(self):
        self.engine = create_engine(
            engine.url.URL.create(
                drivername="postgresql+psycopg2", database=os.environ["POSTGRES_DATABASE"],
                username=os.environ["POSTGRES_USERNAME"], password=os.environ["POSTGRES_PASSWORD"],
                host=os.environ["POSTGRES_HOST"], port=os.environ["POSTGRES_PORT"]
            ),
            pool_size=3, max_overflow=0, pool_recycle=540, pool_pre_ping=True, pool_use_lifo=True
        )

        self.metadata = MetaData(self.engine)

        self.t_users = Table(
            "users", self.metadata,
            Column("id", Integer, primary_key=True, unique=True),
            Column("name", String(128), nullable=False),
            Column("username", String(128), nullable=False, unique=True),
            Column("city", String(128), nullable=False),
            Column("occupation", String(128), nullable=False),
            Column("password", String(128), nullable=False),
        )

        self.metadata.create_all(self.engine, checkfirst=True)

    def create_user(self, user_data):
        with self.engine.begin() as transaction:
            query = self.t_users.insert().values(**dict(user_data)).returning(self.t_users.c.id)

            results = [dict(res) for res in transaction.execute(query)]
        return results[0]

    def get_user(self, user):
        with self.engine.begin() as transaction:
            query = self.t_users.select(
                whereclause=(self.t_users.c.username == user)
            )
            results = [dict(res) for res in transaction.execute(query)]
        return results[0] if len(results) > 0 else None

    def check_status(self):
        try:
            with self.engine.begin() as transaction:
                query = self.t_users.select()
                [dict(res) for res in transaction.execute(query)]
            return True
        except Exception:
            return False


postgres_conn = PostgresConn()
