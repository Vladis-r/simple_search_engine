import json
import os

from elasticsearch import Elasticsearch
from flask.cli import load_dotenv

load_dotenv()

elastic = Elasticsearch(hosts=os.environ.get("ELASTIC_HOST"),
                        basic_auth=(os.environ.get("ELASTIC_USER"), os.environ.get("ELASTIC_PASSWORD")),
                        ssl_assert_fingerprint=os.environ.get("ELASTIC_SSL"))


class ElasticDAO:
    """
    Класс для работы с Эластиком
    """

    def __init__(self, es: Elasticsearch):
        self.es = es

    def create_index(self, index_name: str, mapping: dict, settings: dict) -> None:
        """
        Создать новый индекс
        :param index_name: Имя индекса
        :param mapping: Поля и их типы в индексе
        :param settings: Настройки индекса
        """
        self.es.indices.create(index=index_name, mappings=mapping, settings=settings)

    def add_doc_from_file(self, index, file_json):
        """
        Добавить новый документ в индекс.
        Файл в формате json должен быть добавлен в папку search_engine/data.
        :param index: Имя индекса
        :param file_json: Имя файла
        """
        with open(f"{os.path.abspath('data')}/{file_json}", encoding="utf-8") as file:
            docs = json.load(file)
            for doc in docs:
                self.es.index(index=index, document=doc)

    def add_doc(self, index: str, pk: int, text: str) -> None:
        """
        Добавить документ
        :param index: Имя индекса
        :param pk: ИД документа
        :param text: Текст документа
        """
        self.es.index(index=f"{index}", document={"id": pk, "text": text})

    def search_for_doc(self, index, search_string):
        """
        Поиск по тексту
        :param search_string: Текст
        :return: Список ИД документов
        """
        resp = self.es.search(index=f"{index}", query={"match": {"text": f"{search_string}"}}, size=20)
        search_result = []
        for doc_id in resp["hits"]["hits"]:
            search_result.append(doc_id["_source"]["id"])
        return search_result

    def delete_doc(self, index: str, pk: int):
        """
        Удалить документ по полю ИД в документе.
        :param index: Название индекса.
        :param pk: ИД
        """
        result = self.es.delete_by_query(index=index, query={"match": {"id": f"{pk}"}})
        if result["deleted"] == 0:
            return "Документ не найден"
        else:
            return "Удаление прошло успешно"
