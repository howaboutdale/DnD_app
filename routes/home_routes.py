from flask import Blueprint
from controllers.home_controllers import index, new, create, edit, update, delete

home_routes = Blueprint('home_routes', __name__)

home_routes.route('')(index)
home_routes.route('/new')(new)
home_routes.route('', methods=["POST"])(create)
home_routes.route('/<id>/edit')(edit)
home_routes.route('/<id>', methods=["POST"])(update)
home_routes.route('/<id>/delete', methods=["POST"])(delete)