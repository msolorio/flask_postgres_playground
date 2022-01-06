from flask import Blueprint, jsonify, request
from ..models.Cat import Cat, cat_schema, cats_schema
from ..models import db

cats_bp = Blueprint('cats', __name__)

@cats_bp.route('/')
def index():
    all_cats = Cat.query.all()
    return jsonify(cats_schema.dump(all_cats))


@cats_bp.route('/', methods=['POST'])
def create():
    # TODO: validate request body data

    new_cat = Cat(
        name=request.json.get('name'),
        age=request.json.get('age'),
        color=request.json.get('color')
    )
    db.session.add(new_cat)
    db.session.commit()

    return cat_schema.dump(new_cat)
