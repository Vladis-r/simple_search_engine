from flask_restx import reqparse

parser = reqparse.RequestParser()
parser.add_argument('q', type=str, help='Text query')
