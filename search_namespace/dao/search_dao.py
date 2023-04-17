from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

from db.models import Data


class SearchDAO:
    """
    Класс для работы с БД
    """

    def __init__(self, session: SQLAlchemy):
        self.session = session

    def get_all(self):
        """
        Получить все объекты
        """
        return self.session.query(Data).all()

    def get_by_pk(self, pk: int) -> Data:
        """
        Получить объект по ИД
        """
        return self.session.get(Data, pk)

    def get_objs_by_pk(self, list_pk: list[int]) -> list[Data]:
        """
        Получить объекты по списку с ИД
        """
        docs = self.session.query(Data).filter(Data.id.in_(list_pk)).order_by(desc(Data.created_date)).all()
        return docs

    def del_by_pk(self, pk):
        """
        Удалить объект по ИД
        """
        obj = self.session.get(Data, pk)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            print("Ok")
        else:
            return print("Object not found")
