import pytest

from search_namespace.dao.search_dao import SearchDAO


class TestSearchDAO:

    @pytest.fixture
    def search_dao(self, db):
        return SearchDAO(db.session)

    def test_get_all(self, search_dao):
        assert len(search_dao.get_all()) > 1

    def test_get_by_pk(self, search_dao):
        assert len(search_dao.get_by_pk(5)) == 1
        # assert search_dao.get_by_pk(5) ==