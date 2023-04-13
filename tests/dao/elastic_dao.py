import pytest

from search_namespace.dao.search_dao import SearchDAO


class TestSearchDAO:

    @pytest.fixture
    def search_dao(self, db):
        return SearchDAO(db.session)

    def test_get_all(self, search_dao):
        pass
