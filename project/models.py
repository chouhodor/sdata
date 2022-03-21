from . import db

class Snakes(db.Model):
    __tablename__ = 'snake'
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(50), nullable=True)
    name_bm = db.Column(db.String(50), nullable=True)
    name_scientific = db.Column(db.String(50), nullable=True)
    family = db.Column(db.String(50), nullable=True)
    snake_location = db.Column(db.String(50), nullable=True)
    habitat = db.Column(db.String(50), nullable=True)
    circadian = db.Column(db.String(50), nullable=True)
    venom_status = db.Column(db.String(50), nullable=True)
    antivenom = db.Column(db.String(50), nullable=True)
    iucn = db.Column(db.String(50), nullable=True)
    mybis = db.Column(db.String(50), nullable=True)
    locations = db.relationship('Snake_location', backref = 'location', lazy='dynamic')


class Snake_location(db.Model):
    __tablename__ = 'snake_location'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50), nullable=True)
    snake_id = db.Column(db.Integer, db.ForeignKey('snake.id'))