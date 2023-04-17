import pytest
from elasticsearch import Elasticsearch

from search_namespace.dao.elastic_dao import ElasticDAO

mapping = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "text": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            }
        }
    }
}

INDEX = "test_index"


@pytest.mark.skip(reason="Необходимо настроить отдельный экземпляр Elasticsearch, прежде чем запускать эти тесты")
class TestElasticDAO:

    @pytest.fixture()
    def es(self):
        return ElasticDAO(Elasticsearch(hosts="https://localhost:9200"))

    @pytest.fixture()
    def test_doc(self, es):
        return es.add_doc(index=INDEX, pk=1, text="test")

    def test_connection(self, es):
        assert es.ping is True

    def test_create_index(self, es):
        es.create_index(index_name=INDEX, mapping=mapping, settings=None)
        index = es.indices.get(index=INDEX)
        assert index[INDEX]["mappings"] == mapping

    def test_search_for_doc(self, es, test_doc):
        result = es.search_for_doc(index=INDEX, search_string="tes")
        doc_text = result["hits"]["hits"]["_source"]["text"]
        assert doc_text == "test"

    def test_delete_doc(self, es, test_doc):
        result = es.delete_doc(index=INDEX, pk=1)
        assert result["deleted"] is True
