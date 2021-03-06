from .model_config import db, ma

class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    color = db.Column(db.String(50))

    def __repr__(self):
        return f'<Cat {self.name}>'


class CatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'color')
        model = Cat


cat_schema = CatSchema()
cats_schema = CatSchema(many=True)