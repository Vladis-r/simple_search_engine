from flask import render_template, request, make_response
from flask_restx import Namespace, Resource

from container import elastic_dao, search_dao
from db import api
from db.api_models import data

main_ns = Namespace("main")
search_ns = Namespace("search")


@main_ns.route("/")
class MainView(Resource):
    def get(self):
        """
        Главная страница с поисковой строкой
        """
        return make_response(render_template("search.html"), 200)


@search_ns.route("/")
class SearchView(Resource):
    @search_ns.marshal_with(data, as_list=True, code=200, description="ok")
    @api.doc(query={"q": "строка для поиска"})
    def get(self):
        """
        Поиск в эластике.
        """
        query = request.args.get("q")
        list_of_docs_pk = elastic_dao.search_for_doc("my_index", query)
        response = search_dao.get_docs_by_pk(list_of_docs_pk)

        return response, 200
