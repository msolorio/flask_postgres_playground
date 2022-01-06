from flask import Blueprint, jsonify
from ..models import Cat

cats_bp = Blueprint('cats', __name__)

@cats_bp.route('/')
def index():
    all_cats = Cat.query.all()

    return jsonify(all_cats)
