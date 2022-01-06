from .db import db

class Cat(db.Model):
    __tablename__ = 'cats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    color = db.Column(db.String)

    # @property
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'city': self.city,
    #         'state': self.state,
    #         'address': self.address
    #     }