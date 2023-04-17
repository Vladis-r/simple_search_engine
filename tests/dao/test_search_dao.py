import pytest

from db.models import Data
from search_namespace.dao.search_dao import SearchDAO


class TestSearchDAO:

    @pytest.fixture
    def search_dao(self, db):
        """
        Создаём экземпляр SearchDAO для работы с БД
        """
        return SearchDAO(db.session)

    @pytest.fixture
    def data(self, db):
        db.session.add(Data(text="1 text", rubrics="rubric", created_date="2024-01-01 00:00:00"))
        db.session.add(Data(text="2 text", rubrics="rubric", created_date="2024-01-01 00:00:00"))
        db.session.add(Data(text="3 text", rubrics="rubric", created_date="2024-01-01 00:00:00"))
        db.session.add(Data(text="4 text", rubrics="rubric", created_date="2024-01-01 00:00:00"))
        db.session.add(Data(text="5 text", rubrics="rubric", created_date="2024-01-01 00:00:00"))
        db.session.commit()

    def test_get_all(self, search_dao, data):
        assert len(search_dao.get_all()) > 1

    def test_get_by_pk(self, search_dao, data):
        obj = search_dao.get_by_pk(1)
        assert obj.text == "1 text"

    def test_get_objs_by_pk(self, search_dao, data):
        objs = search_dao.get_objs_by_pk([1, 2])
        assert len(objs) > 1
        assert objs[1].text == "2 text"

    def test_del_by_pk(self, search_dao, data, db):
        search_dao.del_by_pk(1)
        assert search_dao.get_by_pk(1) is None
