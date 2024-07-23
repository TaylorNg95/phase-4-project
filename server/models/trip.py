from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class Trip(db.Model, SerializerMixin):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    total_miles = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Trip id={self.id}, name={self.name}, country={self.country}, miles={self.total_miles}>'

    @validates('name', 'country')
    def validate_inputs(self, key, input):
        if input == '':
            raise ValueError(f'{key} required')
        else:
            return input
        
    @validates('total_miles')
    def validate_total_miles(self, key, total_miles):
        if total_miles <= 0:
            raise ValueError('Total miles must be greater than 0')
        else:
            return total_miles