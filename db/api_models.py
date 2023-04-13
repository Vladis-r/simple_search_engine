from flask_restx import fields, Model

from app import api

data: Model = api.model('Data', {
    'id': fields.Integer(),
    'text': fields.String(),
    'rubrics': fields.String(),
    'created_date': fields.String(),
})
