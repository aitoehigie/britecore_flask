from app import db

class FeatureRequest(db.Model):
    __tablename__ = "feature_request"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    client = db.Column(db.String(64), index=True)
    client_priority = db.Column(db.Integer, default=1)
    target_date = db.Column(db.Date, nullable=False)
    product_area = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<Feature {}>".format(self.title)
