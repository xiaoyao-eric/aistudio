from server import db
from sqlalchemy import JSON, Text


class Region(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=True, index=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20), nullable=False)  # country / province / city / district
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)
    type = db.Column(db.String(50), nullable=True)  # province / municipality / autonomous_region / sar
    sort_order = db.Column(db.Integer, default=0)

    # Travel info (only for locations with rich data)
    badge = db.Column(db.String(200), nullable=True)
    description = db.Column(Text, nullable=True)
    emoji = db.Column(db.String(10), nullable=True)
    attractions = db.Column(JSON, nullable=True)
    food = db.Column(JSON, nullable=True)

    # Relationship
    children = db.relationship(
        'Region', backref=db.backref('parent', remote_side='Region.id'),
        lazy='selectin', order_by='Region.sort_order'
    )

    def to_dict(self, include_children=True):
        d = {
            'id': self.id,
            'parent_id': self.parent_id,
            'name': self.name,
            'level': self.level,
            'lat': self.lat,
            'lng': self.lng,
            'type': self.type,
            'sort_order': self.sort_order,
            'badge': self.badge,
            'description': self.description,
            'emoji': self.emoji,
            'attractions': self.attractions,
            'food': self.food,
        }
        if include_children and self.children:
            d['children'] = [c.to_dict() for c in self.children]
        else:
            d['children'] = []
        return d
