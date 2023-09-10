from sqlalchemy import and_, create_engine
from sqlalchemy import select, insert
from sqlalchemy.orm import sessionmaker
from .dbschema import users_table, User

import logging
from enum import Enum

FORMAT = '%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DBStatus(Enum):
    SUCCESS = 1
    WARNING = 2
    ALREADY_EXIST = 3


class BotDB:
    def __init__(self, path, create_table):
        # Подключение к базе данных через SQLAlchemy
        self.engine = create_engine(f'postgresql+psycopg2://admin:admin@localhost:5432/admin')
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        logger.debug("Connection to DataBase was successfully created!")


    def add_user(self, user: User) -> DBStatus:
        result = DBStatus.SUCCESS

        stmt = insert(users_table).values(user)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        print(result)
        return result
    
    def get_user(self, username):
        stmt = select(users_table)
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                print(row)

    def show_all_users(self):
        stmt = select(users_table)
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                print(row)


    def __del__(self):
        self.session.close()
