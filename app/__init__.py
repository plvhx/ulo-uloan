from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.loader import LoaderFactory
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

app = Flask(__name__)

conf = {
	'db': LoaderFactory().get_database_config().load()
}

app.config['SQLALCHEMY_DATABASE_URI'] = "{0}://{1}:{2}@{3}/{4}".format(
	conf['db']['parameters']['driver'],
	conf['db']['parameters']['username'],
	conf['db']['parameters']['password'],
	conf['db']['parameters']['host'],
	conf['db']['parameters']['database']
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow()

# load all entity
from app.entity.bound import Bound
from app.entity.bound_item import BoundItem
from app.entity.bound_serial import BoundSerial
from app.entity.convert_rule import ConvertRule
from app.entity.item import Item
from app.entity.item_serial import ItemSerial
from app.entity.location import Location

# load all schema
from app.schema.location_schema import LocationSchema
from app.schema.bound_item_schema import BoundItemSchema
from app.schema.bound_serial_schema import BoundSerialSchema
from app.schema.convert_rule_schema import ConvertRuleSchema
from app.schema.item_schema import ItemSchema
from app.schema.item_serial_schema import ItemSerialSchema

# load all resources
from app.resources.location_resource import LocationResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# routes
api.add_resource(LocationResource, '/location')

# register api blueprint
app.register_blueprint(api_bp, url_prefix='/api')
