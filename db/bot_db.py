from sqlalchemy import and_, create_engine
from sqlalchemy import select, insert, delete, update
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
        self.engine = create_engine(f'postgresql://admin:admin@localhost:5432/admin')
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        logger.debug("Connection to DataBase was successfully created!")


    def add_user(self, user: User) -> DBStatus:
        result = DBStatus.SUCCESS

        stmt = insert(users_table).values(user_name=user.user_name,
                                          gender=user.gender,
                                          image=user.image,
                                          email=user.email)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        print(result)
        return result
    
    def get_user(self, username):
        stmt = select(users_table).where(users_table.c.user_name == username)
        users = []
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                users.append(row)
        return users

    def delete_user(self, username):
        stmt = delete(users_table).where(users_table.c.user_name == username)
        return 0

    def update_user(self, user):
        stmt = update(users_table).where(users_table.c.user_name == user.user_name).values(
            user_name=user.user_name,
            gender=user.gender,
            image=user.image,
            email=user.email
        )
        return 0

    def show_all_users(self):
        stmt = select(users_table)
        users = []
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                users.append(row)
        return users
    
    def __del__(self):
        self.session.close()
