import csv
import json

from app import create_app
from container import elastic_dao, search_dao
from db.models import *


def csv_into_db(path):
    """
    Распаковка csv в модель Data.
    path - путь до файла.
    """
    with open(path, encoding="utf-8") as file:
        dr = csv.DictReader(file)
        for row in dr:
            db.session.add(Data(**row))
        db.session.commit()


settings = {
    "index": {
        "number_of_shards": "5"
    }
}

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

# создание и заполнение БД
if __name__ == '__main__':
    with create_app().app_context():
        # Создаём базу данных
        db.create_all()

        # Заполняем БД данными из csv файла
        csv_into_db("../data/posts.csv")

        # Создаём бд в ElasticSearch
        elastic_dao.create_index(index_name="my_index", mapping=mapping, settings=settings)

        # Добавляем данные из БД в эластик
        docs = search_dao.get_objs_by_pk()
        for doc in docs:
            elastic_dao.add_doc(index="my_index", pk=doc.pk, text=doc.text)

        print("Установка прошла успешно!")
