import os

from db import db
from db.models import Data
from search_namespace.dao.elastic_dao import elastic, ElasticDAO
from search_namespace.dao.search_dao import SearchDAO

# DAO
search_dao = SearchDAO(db.session)
elastic_dao = ElasticDAO(elastic)


