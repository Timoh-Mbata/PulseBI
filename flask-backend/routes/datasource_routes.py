from flask import Blueprint, request, jsonify
from models.db_models import db, DataSource

dataSource_blueprint = Blueprint('datasource', __name__)

# CREATE
@dataSource_blueprint.route('/datasources', methods=['POST'])
def create_datasource():
    data = request.get_json()
    new_datasource = DataSource(name=data['name'], description=data.get('description'))
    db.session.add(new_datasource)
    db.session.commit()
    return jsonify({'id': new_datasource.id, 'name': new_datasource.name, 'description': new_datasource.description}), 201

# READ
@dataSource_blueprint.route('/datasources/<int:datasource_id>', methods=['GET'])
def get_datasource(datasource_id):
    datasource = DataSource.query.get_or_404(datasource_id)
    return jsonify({'id': datasource.id, 'name': datasource.name, 'description': datasource.description}), 200

# UPDATE
@dataSource_blueprint.route('/datasources/<int:datasource_id>', methods=['PUT'])
def update_datasource(datasource_id):
    data = request.get_json()
    datasource = DataSource.query.get_or_404(datasource_id)
    datasource.name = data.get('name', datasource.name)
    datasource.description = data.get('description', datasource.description)
    db.session.commit()
    return jsonify({'id': datasource.id, 'name': datasource.name, 'description': datasource.description}), 200

# DELETE
@dataSource_blueprint.route('/datasources/<int:datasource_id>', methods=['DELETE'])
def delete_datasource(datasource_id):
    datasource = DataSource.query.get_or_404(datasource_id)
    db.session.delete(datasource)
    db.session.commit()
    return jsonify(message=f'Datasource {datasource_id} deleted'), 200
